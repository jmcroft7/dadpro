from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template, request, redirect, jsonify, session
from flask import flash
import requests








class Suggestion:
    def __init__(self, data):
        self.id = data['id']
        self.suggestion = data['textarea']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validate_suggestion(data):
        is_valid = True

        if len(request.form['textarea']) < 3 :
            flash('The textarea minimum is 3 characters!', 'textarea')
            is_valid = False
        return is_valid



# ==========================================================
# save registration into a user
    @classmethod
    def save(cls, data):
        query = "INSERT INTO suggestions (id, suggestion, updated_at) VALUES (%(id)s, %(suggestion)s, NOW());"
        results = connectToMySQL("suggestion_schema").query_db(query, data)
        return results