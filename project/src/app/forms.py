from app import cursor
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SelectField, SubmitField, FormField, RadioField, FieldList, DateTimeField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Optional, Length, NumberRange

class TransportForm(FlaskForm):
    transport_type = SelectField('Transport Type', validators=[DataRequired()], choices=[('Airplane', 'Airplane'), ('Bus', 'Bus'), ('Train','Train'), ('Taxi','Taxi/Uber'), ('Ship','Ship'), ('Tram','Tram')])
    start_location = StringField('Starting Location', validators=[DataRequired(), Length(max=64)])
    end_location = StringField('End Location', validators=[DataRequired(), Length(max=64)])

class VisitedAreaMixin():
    area_type = RadioField('Area Type', validators=[DataRequired()], choices=[('event', 'Event'), ('location', 'Location')])
    area_lat = DecimalField('Area Latitude', validators=[Optional()], places=8)
    area_lon = DecimalField('Area Longitude', validators=[Optional()], places=8)
    area_name = StringField('Area Name', validators=[DataRequired(), Length(max=64)])
    area_visitors = IntegerField('Approximate Number of People at the Area')
    
    visit_start_time = DateTimeField('Start Time of the Visit (yyyy-mm-dd HH:MM:SS)')
    visit_end_time = DateTimeField('End Time of the Visit (yyyy-mm-dd HH:MM:SS)')
    transports = FieldList(FormField(TransportForm), min_entries=1)

class VisitedAreaAdd(FlaskForm, VisitedAreaMixin):
    submit = SubmitField('Add Visit')

class VisitedAreaEdit(FlaskForm, VisitedAreaMixin):
    submit = SubmitField('Edit Visit')

class ContractedVirusForm(FlaskForm):
    query = "SELECT Name FROM Virus"
    cursor.execute(query)
    records = [entry[0] for entry in cursor.fetchall()]
    virus = SelectField('Contracted Virus', choices=[('1', records[0]), ('2', records[1]), ('3', records[2]), ('4', records[3])])
    contract_date = DateField('Contract Date', format='%Y-%m-%d', validators=[Optional()])

class PatientMixin():
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=32)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=32)])
    gender = SelectField('Gender', validators=[DataRequired()], choices=[('m', 'Male'), ('f', 'Female')])
    nationality = StringField('Nationality', validators=[Length(min=0, max=32)])
    state = StringField('State', validators=[Length(min=0, max=32)])
    postcode = IntegerField('Postcode', validators=[NumberRange(min=1000, max=9999)])
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[Length(min=0, max=32)])

    viruses = FieldList(FormField(ContractedVirusForm), min_entries=1)
    
class PatientAdd(FlaskForm, PatientMixin):    
    submit = SubmitField('Add Patient')

class PatientEdit(FlaskForm, PatientMixin):    
    submit = SubmitField('Edit Patient')
