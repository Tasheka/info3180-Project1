from app import app, db
from flask import render_template, request, url_for, redirect, flash
from form import NewProfile
from werkzeug.utils import secure_filename
from models import User


import datetime
import os

@app.route("/")
def home():
    return render_template('Home.html')
    
    
@app.route("/profile", methods=["GET", "POST"])
def add_profile():
    form = NewProfile()
    
    if request.method == "POST":
        if form.validate_on_submit():
            try:
                firstName = form.firstName.data
                lastName = form.lastName.data
                gender = form.gender.data
                email = form.email.data
                location = form.location.data
                biography = form.biography.data
                created = str(datetime.datetime.now()).split()[0]
                
                photo = form.profilePhoto.data
                photo_name = secure_filename(photo.filename)
                
                user = User(firstName, lastName, gender, email, location, biography, created, photo_name)                       
                
                db.session.add(user)
                db.session.commit()
        
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'],photo_name))
                
                flash("Profile Added", "success")
                return redirect(url_for("profiles"))
            
            except Exception as e:
                db.session.rollback()
                flash("Internal Error", "danger")
                return render_template("Add Profile.html", form = form)
        
        errors = form_errors(form)
        flash(''.join(error+" " for error in errors), "danger")
    return render_template("Add Profile.html", form = form)


@app.route("/profiles")
def view_profiles():
    users = User.query.all()
    profiles = []
    
    for user in users:
        profiles.append({"pro_pic": user.photo, "f_name":user.firstName, "l_name": user.lastName, "gender": user.gender, "email": user.email,  "location":user.location, "biography": user.biography, "photo": user.photo, "created": user.created})
    
    return render_template("view_profiles.html", profile = profiles)

@app.route('/profile/<userid>')
def inidi_profile(userid):
   # user = User.query.filter_by(id=userid).first()
    
    #if user is None:
#         return redirect(url_for('home'))
        
#     c_y = int(user.created_on.split("-")[0])
#     c_m = int(user.created_on.split("-")[1])
#     c_d = int(user.created_on.split("-")[2])
    
#     user.created_on = format_date_joined(c_y, c_m, c_d)
      return render_template("profile.html",)#user=user)

# def format_date_joined(yy,mm,dd):
#     return datetime.date(yy,mm,dd).strftime("%B, %d,%Y")



def form_errors(form):
    error_list =[]
    for field, errors in form.errors.items():
        for error in errors:
            error_list.append(field+": "+error)
            
    return error_list

@app.route("/about")
def about():
    return render_template("About.html")
    
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404