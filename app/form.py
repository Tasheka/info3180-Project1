from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired,Email
from flask_wtf.file import FileAllowed, FileRequired, FileField 
from flask import Flask, render_template, flash, session, redirect, url_for
from wtforms import TextAreaField, TextField, SubmitField, SelectField

class NewProfile(FlaskForm):
      firstName = StringField("First Name", validators=[InputRequired()])
      lastName = StringField("Last Name", validators=[InputRequired()])
      gender = SelectField("Gender", choices=[("None", "Select Gender"), ("Male", "Male"), ("Female", "Female")], validators=[InputRequired()])
      email = StringField("Email", validators = [InputRequired(), Email()])
      location = StringField("Location", validators = [InputRequired()])
      biography = TextAreaField("Biography", validators = [InputRequired()])
      profilePhoto = FileField("Profile Picture", validators=[FileRequired(), FileAllowed(['jpg', 'png','jpeg'], 'Images Only')])    
 