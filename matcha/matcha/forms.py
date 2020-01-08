from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from matcha.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    first_name = StringField('First_Name', validators=[DataRequired(),Length(min=3, max=50)])
    last_name = StringField('Last_Name', validators=[DataRequired(),Length(min=3, max=50)])                        
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8)])
    confirm_password = PasswordField('Confirm_Password', 
    validators=[DataRequired(),Length(min=8), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('The username already exits please choose another one')

    def validate_email(self, email):
        
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email already exits please choose another one')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign in')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('The username already exits please choose another one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email already exits please choose another one')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first. ')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8)])
    confirm_password = PasswordField('Confirm_Password', validators=[DataRequired(),Length(min=8), EqualTo('password')])
    submit = SubmitField('Reset Password')

   