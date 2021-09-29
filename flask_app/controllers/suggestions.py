from flask_app.models.suggestion import Suggestion
from flask_app import app
from flask import render_template, request, redirect, jsonify, session
from flask import flash
import requests

from flask_app.controllers.users import User
from flask_app.models.joke import Joke
from flask_app.models.author import Author






# ======================================================
# Suggestion route
@app.route('/suggestion')
def suggestion():
        if "user_id" in session:
            data = {
                'id': session['user_id']
            }
            usercolor = User.user_info(data)
            return render_template('suggestions2.html', usercolor=usercolor)
        return render_template('suggestions.html')



# ======================================================
# Suggestion function route
@app.route('/submitinfo', methods=['POST'])
def submitinfo():
        if "user_id" not in session:
            flash("Please register/login before submitting a suggestion", 'notlogged')
            return redirect('/suggestion')
        data = {
            'id': session['user_id'],
            'textarea': request.form['textarea']
        }
        if Suggestion.validate_suggestion(data) == False:
            return redirect('/suggestion')
        flash('Thank you, Your suggestion will be reviewed!', 'loggedforreal')
        return redirect('/suggestion')