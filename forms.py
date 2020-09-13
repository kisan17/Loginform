from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,length,Email,EqualTo,Length
class Registrationform(FlaskForm):
	username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	Email=StringField('Email',validators=[DataRequired(),Email()])
	Password=PasswordField('Password',validators=[DataRequired()])
	Confirm_password=PasswordField('Confirm password',validators=[DataRequired(),EqualTo('Password')])
	Submit=SubmitField('sign up')

class Loginform(FlaskForm):
	Email=StringField('Email',validators=[DataRequired(),Email()])
	Password=PasswordField('Password',validators=[DataRequired()])
	remember=BooleanField('Remember Me')
	Submit=SubmitField('login')