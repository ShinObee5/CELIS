from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,RadioField,SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired,Email,EqualTo


class LoginForm(FlaskForm):
    username=EmailField('Username',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    conpassword=PasswordField('Re-Enter Password',validators=[DataRequired(),EqualTo('password')])#('values','label')
    user_role=RadioField('User Role',validators=[DataRequired()],choices=[('Student','Student'),('Instructor','Instructor')])
    Region=SelectField('Select Region',validators=[(DataRequired())],choices=[('USA','USA'),('India','India'),('America','America')])
    submit=SubmitField('Sign In')
