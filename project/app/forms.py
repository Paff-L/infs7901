from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired

class PatientForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender', validators=[DataRequired()], choices=[('m', 'f')])
    nationality = StringField('Nationality')
    state = StringField('State')
    postcode = IntegerField('Postcode')
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    phone_number = StringField('Phone Number')
    submit = SubmitField('Add Patient')