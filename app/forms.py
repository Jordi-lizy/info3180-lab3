from flask_wtf import *
from wtforms import *
#from wtforms import EmailField
#from wtforms import TextAreaField
#from wtforms import SubmitField
#from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', [validators.Length(min = 5, max =22), validators.DataRequired()])
    email = StringField('Email',[validators. Email(), validators.DataRequired()])
    subject = StringField('Subject', [validators.Length(min = 1, max = 20), validators.DataRequired()])
    message = TextAreaField('Message', [validators.Length(max = 255), validators.DataRequired()])
    #csrf_token = csrf.CSRFProtect()
    submit = SubmitField('Send')

