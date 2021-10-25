from indepProject import app
from flask import render_template, session, request, flash, redirect, url_for
from .models.shared import db
from .models import User
from .tools import Insert_enrollment 

@app.route('/')
def home():
  if 'username' in session:
    headers=[]
    data_list=[]
    Insert_enrollment(1,3595946,"sectionTest","A+")
    # Render templates
    return render_template('home.html',usergroup=session['usergroup'].capitalize())
  return render_template('login.html')
    

# Login path sends to login page
@app.route('/login', methods=['GET','POST'])
def login_user():
  if request.method=="POST":
    mail=request.form['email']
    pw=request.form['password']
    current_user=User.query.filter_by(email=mail,password=pw).first()
    
    if current_user is not None:
      session['username']=mail
      session['usergroup']=current_user.usergroup
      return redirect(url_for("home"))
  return render_template('login.html')

# Register path sends to register page
@app.route("/register", methods=['GET','POST'])
def register_user():
  if request.method=="POST":
    mail=request.form['email']
    pw=request.form['password']

    #check if user is already registered
    if User.query.filter_by(email=mail).first():
      flash('Email is already in use','error')
    # TODO change these arbitrary check conditions
    elif len(mail)<5:
      flash('Email is invalid','error')
    elif len(pw)<6:
      flash('Password must be at least 6 characters','error')
    else:
      register=User(email=mail,password=pw)
      db.session.add(register)
      db.session.commit()
      return redirect(url_for("login_user"))
  return render_template('register.html')

# Logout path returns home
@app.route("/logout")
def logout():
  session.pop('username',None)
  return redirect(url_for("home"))