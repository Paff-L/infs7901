from app import cursor
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField, DateField, FormField, FieldList
from wtforms.validators import DataRequired, Length, NumberRange

class ContractedVirusForm(FlaskForm):
    query = "SELECT Name FROM Virus"
    cursor.execute(query)
    records = [entry[0] for entry in cursor.fetchall()]
    virus = SelectField('Contracted Virus', choices=[(1, records[0]), (2, records[1]), (3, records[2]), (4, records[3])])

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
