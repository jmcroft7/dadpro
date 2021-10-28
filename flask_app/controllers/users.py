from flask_app import app
from flask import render_template, request, redirect, jsonify, session
from flask import flash
import requests

from flask_app.models.user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


# ========================================================
# Login page
@app.route('/login')
def login():
        return render_template('login.html')


# ========================================================
# Register route
@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/login')
# checks if email already exists
    data1 = {
        'email' : request.form['email']
    }
    if User.get_by_email(data1):
        flash('Email already exists!', 'already')
        return redirect('/login')
# encrypts password before saving it
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
# save data also store session
    new_user_id = User.save(data)
    flash('Successfully created an account!', 'success')
    session['user_id'] = new_user_id
    return redirect('/login')


# ======================================================
# login authentication route
@app.route('/loginauth', methods=['POST'])
def loginauth():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # if email doesn't exist in db
    if not user_in_db:
        flash("Invalid Credentials | No email found!", 'none')
        return redirect("/login")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Credentials | password incorrect!", 'wrong')
        return redirect('/login')
    # we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/")


# ======================================================
# logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# ======================================================
# delete route
@app.route('/delete')
def deleteMe():
    if "user_id" in session:
        data = {
        'id': session['user_id']
        }
    User.deleteUser(data)
    session.clear()
    return redirect('/')


# ======================================================
# Settings route
@app.route('/settings')
def settings():
    if "user_id" not in session:
        flash("Please register/login before editing settings", 'missing')
        return redirect('/login')
    data = {
        'id' : session['user_id']
    }
    usercolor = User.user_info(data)
    return render_template('settings.html', usercolor=usercolor)


# ======================================================
# Settings function route
@app.route('/settingsupdate', methods=['POST'])
def updatesettings():
    if "user_id" not in session:
        flash("Please register/login before editing settings", 'missing')
        return redirect('/login')
    data = {
        'keycolor' : request.form['keycolor'],
        'id' : session['user_id']
    }
    User.updateUser(data)
    flash('Settings have been successfully updated!', 'settingschanged')
    return redirect('/')