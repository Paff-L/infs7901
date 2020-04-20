from flask import render_template, flash, redirect, url_for
from app import app, cursor, db
from app.forms import PatientAdd, PatientEdit
from app.models import Patient

@app.route('/')
@app.route('/index')
def index():
    query = "SELECT * FROM Patient"
    cursor.execute(query)
    records = cursor.fetchall()
    return render_template('index.html', title='Home')

@app.route('/patient/<patient_id>')
def patient(patient_id):
    query = f"SELECT * FROM Patient WHERE PatientID = {patient_id}"
    cursor.execute(query)
    patient_info = cursor.fetchall()
    
    query = f"SELECT V.VirusID, V.Name FROM Contracted C, Virus V WHERE C.VirusID = V.VirusID AND C.PatientID = {patient_id}"
    cursor.execute(query)
    contracted_viruses = cursor.fetchall()
    return render_template('patient.html', title=f'Patient Number: {patient_id}', patient=patient_info[0], viruses=contracted_viruses)

@app.route('/patients')
def patients():
    query = "SELECT * FROM Patient"
    cursor.execute(query)
    records = cursor.fetchall()
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
        return redirect(url_for('index'))
    return render_template('add_patient.html', title='Add Patient', form=form)

@app.route('/patient/<patient_id>/edit', methods=['GET', 'POST'])
def edit_patient(patient_id):
    form = PatientEdit()
    
    if not form.is_submitted():
        query = f"SELECT * FROM Patient WHERE PatientID = {patient_id}"
        cursor.execute(query)
        records = cursor.fetchall()
        patient_info = Patient(records[0])
        form.process(obj=patient_info)
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
        return redirect(url_for('patient', patient_id=patient_id))
    return render_template('edit_patient.html', title='Edit Patient Information', form=form)

@app.route('/virus/<virus_id>')
def virus(virus_id):
    query = f"SELECT * FROM Virus WHERE VirusID = {virus_id}"
    cursor.execute(query)
    virus_info = cursor.fetchall()[0]
    print(virus_info)
    return render_template('virus.html', title=f'{virus_info[1]}', virus=virus_info)

@app.route('/viruses')
def viruses():
    query = "SELECT * FROM Virus"
    cursor.execute(query)
    records = cursor.fetchall()
    return render_template('viruses.html', title='Viruses', viruses=records)

