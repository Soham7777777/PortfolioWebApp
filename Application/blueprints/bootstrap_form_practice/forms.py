from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField, EmailField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ReadOnly, ValidationError
from icecream import ic

def validate_phone_no(form, field):
    try:
        int(field.data)
    except ValueError:
        raise ValidationError('This field can only contain numbers')


class StudentRegistrationForm(FlaskForm):
    fname = StringField('Firstname:', validators=[DataRequired(), Length(min=2, max=20)], default='', filters=[str.strip, str.lower], render_kw=dict(placeholder='Firstname'))

    mname = StringField('Middlename:', validators=[DataRequired(), Length(min=2, max=20)], default='', filters=[str.strip, str.lower], render_kw=dict(placeholder='Middlename'))

    lname = StringField('Lastname:', validators=[DataRequired(), Length(min=2, max=20)], default='', filters=[str.strip, str.lower], render_kw=dict(placeholder='Lastname'))

    course = SelectField('Course:', validators=[DataRequired()], choices=[('btech','BTech'), ('bca', 'BCA'), ('mca', 'MCA')], default='btech')

    gender = RadioField('Gender:', validators=[DataRequired()], choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male')

    country_code = StringField('Country Code', default='+91', validators=[ReadOnly()])

    phone_no = StringField('Phone:', validators=[DataRequired(), Length(min=10, max=10), validate_phone_no], default='', filters=[str.strip], render_kw=dict(placeholder='phone no.'))

    current_address = TextAreaField('Current Address:', render_kw=dict(rows='5', placeholder='Current Address'), validators=[DataRequired(), Length(min=10, max=300)], default='', filters=[str.strip, str.lower])

    email = EmailField('Email:', validators=[DataRequired(), Length(min=3, max=320)], default='', filters=[str.strip], render_kw=dict(placeholder='Enter Email'))

    password = PasswordField('Password:', validators=[DataRequired(), Length(min=8, max=16)], default='', filters=[str.strip], render_kw=dict(placeholder='Enter Password'))

    re_password = PasswordField('Re-type Password:', validators=[DataRequired(), Length(min=8, max=16), EqualTo('password', 'passwords are not matching')], default='', filters=[str.strip], render_kw=dict(placeholder='Retype Password'))

    submit = SubmitField('Register')