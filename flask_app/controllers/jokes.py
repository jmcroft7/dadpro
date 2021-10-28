from flask_app import app
from flask import render_template, request, redirect, jsonify, session
from flask import flash
import requests

from flask_app.controllers.users import User
from flask_app.models.joke import Joke
from flask_app.models.author import Author


# ======================================================
# Index route
@app.route('/')
def index():
    if "user_id" in session:
        data = {
            'id': session['user_id']
        }
        usercolor = User.user_info(data)
        joke = Joke.getquote()
        char = Author.getauthor()
        return render_template('index2.html', joke=joke, usercolor=usercolor, char=char)
    joke = Joke.getquote()
    char = Author.getauthor()
    return render_template('index.html', joke=joke, char=char)


# ======================================================
# Random route
@app.route('/random')
def indexRandom():
    return redirect('/')


# ======================================================
# Search route
@app.route('/search')
def search():
    if "user_id" in session:
        data = {
            'id': session['user_id']
        }
        usercolor = User.user_info(data)
        jokes = Joke.getlist()
        return render_template('search2.html', jokes=jokes, usercolor=usercolor)
    jokes = Joke.getlist()
    return render_template('search.html', jokes=jokes)


# ======================================================
# Search function route
@app.route('/searchterms', methods=['POST'])
def searchTerms():
    session['keyword'] = request.form['keyword']
    return redirect('/searchterm')


# ======================================================
# Search by keyword route
@app.route('/searchterm')
def search2():
    if "user_id" in session:
        data = {
            'id': session['user_id']
        }
        data2 = {
            'keyword': session['keyword']
        }
        usercolor = User.user_info(data)
        joke = Joke.searching(data2)
        count = Joke.counting(data2)
        return render_template('searchitem2.html', jokes=joke, count=count, usercolor=usercolor)
    data = {
        'keyword': session['keyword']
    }
    joke = Joke.searching(data)
    count = Joke.counting(data)
    return render_template('searchitem.html', jokes=joke, count=count)
