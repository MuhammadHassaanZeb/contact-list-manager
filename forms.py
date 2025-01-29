from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class ContactForm(FlaskForm):
    name = StringField('Name')
    phone = StringField('Phone',
                        validators=[
                            DataRequired(),
                            Length(min=8, max=8, message="Invalid phone number, please enter only 8 digits!")
                            ]
                        )

    email = StringField('Email')
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Other', 'Other')])
    submit = SubmitField('Submit') 