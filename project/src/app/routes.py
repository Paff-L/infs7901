from datetime import date
from flask import render_template, flash, redirect, url_for
from app import app, cursor, db
from app.forms import PatientAdd, PatientEdit, ContractedVirusForm, VisitedAreaAdd
from app.models import Patient

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/patient/<patient_id>')
def patient(patient_id):
    query = f"SELECT * FROM Patient WHERE PatientID = {patient_id}"
    cursor.execute(query)
    patient_info = cursor.fetchall()

    query = f"SELECT * FROM HighRiskContact WHERE PatientID = {patient_id}"
    cursor.execute(query)
    high_risk_contacts = cursor.fetchall()

    query = f"SELECT V.VirusID, V.Name FROM Contracted C, Virus V WHERE C.VirusID = V.VirusID AND C.PatientID = {patient_id}"
    cursor.execute(query)
    contracted_viruses = cursor.fetchall()

    query = f"SELECT AreaID, StartTime FROM Visited WHERE PatientID = {patient_id}"
    cursor.execute(query)
    visited_areas = cursor.fetchall()

    location_names = []
    for area_id in [area[0] for area in visited_areas]:
        query = f"(SELECT Name FROM Location WHERE AreaID = {area_id}) \
                UNION \
                (SELECT Name FROM Event WHERE AreaID = {area_id})"
        cursor.execute(query)
        location_names.append(cursor.fetchall()[0][0])

    for i, name in enumerate(location_names):
        visited_areas[i] = visited_areas[i] + (name,)
    visited_areas = list(set(visited_areas))

    return render_template('patient.html', title=f'Patient Number: {patient_id}', patient=patient_info[0], contacts=high_risk_contacts, viruses=contracted_viruses, visits=visited_areas)

@app.route('/patients')
def patients():
    query = "SELECT * FROM Patient"
    cursor.execute(query)
    records = cursor.fetchall()
    for i, record in enumerate(records):
        dob = record[7]
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        records[i] = record + (age,)
    return render_template('patients.html', title='Patients', patients=records)

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    form = PatientAdd()
    if form.validate_on_submit():
        flash(f'Patient {form.first_name.data} successfully recorded.')
        query = f"INSERT INTO `Patient` (`FirstName`, `LastName`, `Gender`, `Nationality`, `State`, `Postcode`, `DOB`, `PhoneNumber`) VALUES \
                (%s, %s, %s, %s, %s, %s, %s, %s)"
        data_list = [entry.data for entry in form]
        cursor.execute(query, data_list[:8])
        db.commit()

        query = f"SELECT PatientID FROM Patient WHERE FirstName = '{form.first_name.data}' AND LastName = '{form.last_name.data}' AND DOB = '{form.date_of_birth.data}'"
        cursor.execute(query)
        records = cursor.fetchall()
        patient_id = records[0][0]

        for entry in form.viruses.data:
            virus_id = int(entry.get('virus'))
            contract_date = entry.get('contract_date')
            query = f"INSERT INTO `Contracted` (`PatientID`, `VirusID`, `ContractDate`) VALUES \
                    (%s, %s, %s)"
            data_list = [patient_id, virus_id, contract_date]
            cursor.execute(query, data_list)
            db.commit()

        return redirect(url_for('patients'))
    return render_template('add_patient.html', title='Add Patient', form=form)

@app.route('/patient/<patient_id>/edit', methods=['GET', 'POST'])
def edit_patient(patient_id):
    form = PatientEdit()

    query = f"SELECT * FROM Patient WHERE PatientID = {patient_id}"
    cursor.execute(query)
    records = cursor.fetchall()

    query = f"SELECT V.VirusID, C.ContractDate FROM Contracted C, Virus V WHERE C.VirusID = V.VirusID AND C.PatientID = {patient_id}"
    cursor.execute(query)
    contracted_viruses = cursor.fetchall()

    if not form.is_submitted():
        patient_info = Patient(records[0])
        form.process(obj=patient_info)
        if contracted_viruses:
            form.viruses.pop_entry()
        for virus_id, contract_date in [entry for entry in contracted_viruses]:
            virus_form = ContractedVirusForm()
            virus_form.virus = virus_id
            virus_form.contract_date = contract_date
            form.viruses.append_entry(virus_form)
    else:
        form = PatientEdit()

    if form.validate_on_submit():
        flash(f'Patient {form.first_name.data} successfully edited.')
        query = f"Update `Patient` SET `FirstName` = '{form.first_name.data}', \
                `LastName` = '{form.last_name.data}', \
                `Gender` = '{form.gender.data}', \
                `Nationality` = '{form.nationality.data}', \
                `State` = '{form.state.data}', \
                `Postcode` = '{form.postcode.data}', \
                `DOB` = '{form.date_of_birth.data}', \
                `PhoneNumber` = '{form.phone_number.data}' WHERE PatientID = {patient_id}"
        cursor.execute(query)
        db.commit()

        for entry in form.viruses.data:
            virus_id = int(entry.get('virus'))
            contract_date = entry.get('contract_date')
            if virus_id not in [entry[0] for entry in contracted_viruses]:
                query = f"INSERT INTO `Contracted` (`PatientID`, `VirusID`, `ContractDate`) VALUES \
                        (%s, %s, %s)"
                data_list = [patient_id, virus_id, contract_date]
                cursor.execute(query, data_list)
                db.commit()
            else:
                if contract_date != [entry[1] for entry in contracted_viruses if entry[0] == virus_id][0]:
                    query = f"UPDATE `Contracted` SET `ContractDate` = '{contract_date}' \
                            WHERE PatientID = {patient_id} AND VirusID = {virus_id}"
                    cursor.execute(query)
                    db.commit()

        # Delete entries that has been marked as cured
        for entry in contracted_viruses:
            if str(entry[0]) not in [form_data.get('virus') for form_data in form.viruses.data]:
                query = f"DELETE FROM `Contracted` WHERE PatientID = '{patient_id}' AND VirusID = '{entry[0]}'"
                cursor.execute(query)
                db.commit()
        return redirect(url_for('patient', patient_id=patient_id))
    return render_template('edit_patient.html', title='Edit Patient Information', form=form)

@app.route('/virus/<virus_id>')
def virus(virus_id):
    query = f"SELECT * FROM Virus WHERE VirusID = {virus_id}"
    cursor.execute(query)
    virus_info = cursor.fetchall()[0]
    return render_template('virus.html', title=f'{virus_info[1]}', virus=virus_info)

@app.route('/viruses')
def viruses():
    query = "SELECT * FROM Virus"
    cursor.execute(query)
    records = cursor.fetchall()
    return render_template('viruses.html', title='Viruses', viruses=records)

@app.route('/areas')
def areas():
    locations = []
    query = "SELECT L.Name, L.AvgVisitors, P.FirstName, P.LastName, V.StartTime, V.EndTime, P.PatientID, V.AreaID \
            FROM Location L, Patient P, Visited V \
            WHERE V.PatientID = P.PatientID AND V.AreaID = L.AreaID"
    cursor.execute(query)
    records = cursor.fetchall()
    used = set()
    for record in [x for x in records if x not in used and (used.add(x) or True)]:
        if record[0] in [location[0] for location in locations]:
            locations[-1][-1].append(record[2:])
        else:
            locations.append([record[0], record[1], [record[2:]]])

    events = []
    query = "SELECT E.Name, E.TotalVisitors, P.FirstName, P.LastName, V.StartTime, V.EndTime, P.PatientID, V.AreaID \
            FROM Event E, Patient P, Visited V \
            WHERE V.PatientID = P.PatientID AND V.AreaID = E.AreaID"
    cursor.execute(query)
    records = cursor.fetchall()
    used = set()
    for record in [x for x in records if x not in used and (used.add(x) or True)]:
        if record[0] in [event[0] for event in events]:
            events[-1][-1].append(record[2:])
        else:
            events.append([record[0], record[1], [record[2:]]])
    return render_template('areas.html', title='Areas', locations=locations, events=events)

@app.route('/visit/patient_id=<patient_id>+area_id=<area_id>+start_time=<start_time>')
def visit(patient_id, area_id, start_time):
    query = f"SELECT P.FirstName, V.VisitID \
            FROM Patient P, Visited V \
            WHERE V.PatientID = {patient_id} \
            AND V.PatientID = P.PatientID \
            AND V.AreaID = {area_id} \
            AND V.StartTime = '{start_time}'"
    cursor.execute(query)
    records = cursor.fetchall()
    visited_ids = [id[1] for id in records]
    patient_name = records[0][0]

    transports=[]
    for visit_id in visited_ids:
        query = f"SELECT T.TransportType, T.StartLocation, T.EndLocation \
                FROM Patient P, Transport T, Visited V \
                WHERE V.VisitID = {visit_id} \
                AND P.PatientID = V.PatientID \
                AND T.TransportID = V.TransportID"
        cursor.execute(query)
        records = cursor.fetchall()
        if records:
            transports.append(records[0])
    transports = list(set(transports))

    query = f"(SELECT Name FROM Location WHERE AreaID = {area_id}) \
            UNION \
            (SELECT Name FROM Event WHERE AreaID = {area_id})"
    cursor.execute(query)
    location_name = cursor.fetchall()[0][0]

    return render_template('visit.html', title=f"{patient_name}'s visit to {location_name}", name=patient_name, location=location_name, start_date=start_time, transports=transports)

@app.route('/patient/<patient_id>/add_visit', methods=['GET', 'POST'])
def add_visit(patient_id):
    form = VisitedAreaAdd()
    query = f"SELECT FirstName FROM Patient WHERE PatientID = {patient_id}"
    cursor.execute(query)
    patient_name = cursor.fetchall()[0][0]

    if form.validate_on_submit():
        flash(f"{patient_name}'s visit to {form.area_name.data} successfully recorded.")

        # Find if existing location/event exists
        if form.area_type.data == 'location':
            query = f"SELECT AreaID FROM Location WHERE Name = '{form.area_name.data}'"
            cursor.execute(query)
            location_match = cursor.fetchall()

            # If the location does not exist
            if not location_match:
                query = f"INSERT INTO `Area` (`Latitude`, `Longitude`) VALUES \
                        (%s, %s)"
                data_list = [form.area_lat.data, form.area_lon.data]
                cursor.execute(query, data_list)
                db.commit()
                area_id = cursor.lastrowid

                query = f"INSERT INTO `Location` (`AreaID`, `Name`, `AvgVisitors`) VALUES \
                        (%s, %s, %s)"
                data_list = [area_id, form.area_name.data, form.area_visitors.data]
                cursor.execute(query, data_list)
                db.commit()
            else:
                area_id = location_match[0][0]
        else:
            query = f"SELECT AreaID FROM Event WHERE Name = '{form.area_name.data}'"
            cursor.execute(query)
            event_match = cursor.fetchall()

            # If the event does not exist
            if not event_match:
                query = f"INSERT INTO `Area` (`Latitude`, `Longitude`) VALUES \
                        (%s, %s)"
                data_list = [form.area_lat.data, form.area_lon.data]
                cursor.execute(query, data_list)
                db.commit()
                area_id = cursor.lastrowid

                query = f"INSERT INTO `Event` (`AreaID`, `Name`, `TotalVisitors`) VALUES \
                        (%s, %s, %s)"
                data_list = [area_id, form.area_name.data, form.area_visitors.data]
                cursor.execute(query, data_list)
                db.commit()
            else:
                area_id = event_match[0][0]


        # Parse transport data
        transports = form.transports.data
        if len(transports) == 1 and transports[0].get('start_location') == 'None' and transports[0].get('end_location') == 'None':
            transport_id = None
            # Add data to visited table
            query = f"INSERT INTO `Visited` (`PatientID`, `TransportID`, `AreaID`, `StartTime`, `EndTime`) VALUES \
                    (%s, %s, %s, %s, %s)"
            data_list = [patient_id, transport_id, area_id, form.visit_start_time.data, form.visit_end_time.data]
            cursor.execute(query, data_list)
            db.commit()
        else:
            for transport in transports:
                query = f'''SELECT TransportID FROM Transport \
                        WHERE TransportType = "{transport.get('transport_type')}" \
                        AND StartLocation = "{transport.get('start_location')}" \
                        AND EndLocation = "{transport.get('end_location')}"'''
                cursor.execute(query)
                transport_match = cursor.fetchall()
                if transport_match:
                    transport_id = transport_match[0][0]
                else:
                    query = f"INSERT INTO `Transport` (`TransportType`, `StartLocation`, `EndLocation`) VALUES \
                            (%s, %s, %s)"
                    data_list = [transport.get('transport_type'), transport.get('start_location'), transport.get('end_location')]
                    cursor.execute(query, data_list)
                    db.commit()
                    transport_id = cursor.lastrowid

                # Add data to visited table
                query = f"INSERT INTO `Visited` (`PatientID`, `TransportID`, `AreaID`, `StartTime`, `EndTime`) VALUES \
                        (%s, %s, %s, %s, %s)"
                data_list = [patient_id, transport_id, area_id, form.visit_start_time.data, form.visit_end_time.data]
                cursor.execute(query, data_list)
                db.commit()

        return redirect(url_for('patient', patient_id=patient_id))
    return render_template('add_visit.html', title='Add Visit', form=form)
