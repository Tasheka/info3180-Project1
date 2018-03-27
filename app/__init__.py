from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='ilOvEmE'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://tasheka-project1:thisispassword@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
UPLOAD_FOLDER = './app/static/uploads'
db = SQLAlchemy(app)

from app import views


# app = Flask(__name__)
# app.config['SECRET_KEY'] = "SuperSecretKey"
# #app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://fmnibhaashbxuy:73b8e2e2485adfd45f57da653d63950b88fdcae12202a84f80c7f4c297e9e30a@ec2-23-23-222-184.compute-1.amazonaws.com:5432/d27ig8fpt4ch7r"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://info2180-project1:password123@localhost/profilebook"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
# app.config['UPLOAD_FOLDER'] = './app/static/profile_photo'
# db = SQLAlchemy(app)

# allowed_exts = ["jpg", "jpeg", "png"]

# from app import views