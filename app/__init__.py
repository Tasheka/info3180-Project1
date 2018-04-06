from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='ilOvEmE'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://tasheka-project1:thisispassword@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/photos'
db = SQLAlchemy(app)

from app import views

