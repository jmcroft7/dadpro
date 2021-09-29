from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)




# class for User
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.bg_color = data['bg_color']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



# staticmethods
# =============================================
    @staticmethod
    def validate_user(data):
        is_valid = True

        if len(data['first_name']) < 2:
            flash('The first name minimum length is 3 characters!', 'firstname')
            is_valid = False

        if len(data['last_name']) < 2:
            flash('The last name minimum length is 3 characters!', 'lastname')
            is_valid = False

        if len(data['email']) < 6:
            flash('The email minimum must be at least 7 characters long to be valid!', 'email')
            is_valid = False

        if not EMAIL_REGEX.match(data['email']):
            flash('Email is not valid! make sure it has an @ symbol and a .com/net/org etc!')
            is_valid = False

        if len(data['password']) < 7:
            flash('The password minimum must be at least 8 characters long!', 'password')
            is_valid = False

        if data['conpass'] != data['password']:
            flash('The passwords must match!', 'password2')
            is_valid = False
        return is_valid



# classmethods
# ==========================================================
# check if email already exists
    @classmethod
    def get_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL('dadjoke_clone').query_db(query, data)
        # didnt find a matching user
        if len(results) < 1:
            return False
        return cls(results[0])



# ==========================================================
# save registration into a user
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW());"
        results = connectToMySQL("dadjoke_clone").query_db(query, data)
        return results



# ==========================================================
# retrieve user info
    @classmethod
    def user_info(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL('dadjoke_clone').query_db(query, data)
        return cls(results[0])



# ==========================================================
# update user info
    @classmethod
    def updateUser(cls, data):
        query = "UPDATE users SET bg_color = %(keycolor)s, updated_at = NOW() WHERE id = %(id)s;"
        results = connectToMySQL('dadjoke_clone').query_db(query, data)
        return results


# ==========================================================
# delete user info
    @classmethod
    def deleteUser(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        results = connectToMySQL('dadjoke_clone').query_db(query, data)
        return results