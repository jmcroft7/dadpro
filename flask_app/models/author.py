from flask_app import app
from flask import render_template, request, redirect, jsonify, session
from flask import flash
import requests









# class for User
class Author:
    def __init__(self, id, contents):
        self.id = id
        self.contents = contents



# classmethods
# ==========================================================
# retrieve office character name
    @classmethod
    def getauthor(cls):
        rawauthor = requests.get('https://officeapi.dev/api/characters/random')
        words2 = rawauthor.json()
        print(words2['data'])
        endauthor = words2['data']
        return endauthor