from flask import render_template, flash, redirect, url_for
from app import app, cursor, db
from app.forms import PatientForm

@app.route('/')
@app.route('/index')
def index():
    query = "SELECT * FROM Patient"
    cursor.execute(query)
    records = cursor.fetchall()
    return render_template('index.html', title='Home', patients=records)

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    form = PatientForm()
    if form.validate_on_submit():
        flash(f'Patient {form.first_name.data} successfully recorded.')
        query = f"INSERT INTO `Patient` (`FirstName`, `LastName`, `Gender`, `Nationality`, `State`, `Postcode`, `DOB`, `PhoneNumber`) VALUES \
                (%s, %s, %s, %s, %s, %s, %s, %s)"
        data_list = [entry.data for entry in form]
        cursor.execute(query, data_list[:8])
        db.commit()
        return redirect(url_for('index'))
    return render_template('add_patient.html', title='Add Patient', form=form)