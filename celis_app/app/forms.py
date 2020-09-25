from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,RadioField,SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired,Email,EqualTo


class LoginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()],render_kw={'class':'form-control form-group'})
    email=EmailField('Email',validators=[DataRequired(),Email()],render_kw={'class':'form-control form-group'})
    password=PasswordField('Password',validators=[DataRequired()],render_kw={'class':'form-control form-group'})
    conpassword=PasswordField('Re-Enter Password',validators=[DataRequired(),EqualTo('password')],render_kw={'class':'form-control form-group'})#('values','label')
    user_role=RadioField('User Role',validators=[DataRequired()],choices=[('Student','Student'),('Instructor','Instructor')],render_kw={'class':'form-check form-check-input','style':'list-style:none;'})
    Region=SelectField('Select Region',validators=[(DataRequired())],choices=[('USA','USA'),('India','India'),('America','America')],render_kw={'class':'form-group col-md-4 form-control '})
    # remember_me=BooleanField('Keep Me Signed In')
    submit=SubmitField('Sign In',render_kw={'class':'btn btn-primary','style':'height : 50px;'})
