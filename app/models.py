from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firsName = db.Column(db.String(80))
    lastName = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(120), unique=True)
    location =  db.Column(db.String(50))
    biography = db.Column(db.String(255))
    photo = db.Column(db.String(80))
    created = db.Column(db.String(80))
    
    __tablename__ = "users"
    
    def __init__(self,firstName,lastName,gender,email,location,biography,created,photo):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.created = created
        self.photo = photo
    
    def __repr__(self):
        return "User: {0} {1}".format(self.firstName, self.lastName)
        
    