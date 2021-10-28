from flask_app import app
from flask import render_template, request, redirect, jsonify, session
from flask import flash
import requests


# class for User
class Joke:
    def __init__(self, id, contents):
        self.id = id
        self.contents = contents


# classmethods
# ==========================================================
# retrieve joke
    @classmethod
    def getquote(cls):
        rawjoke = requests.get('https://icanhazdadjoke.com', headers={"Accept": "application/json"})
        words = rawjoke.json()
        print(words)
        endjoke = words['joke']
        return endjoke


# ==========================================================
# get list of jokes
    @classmethod
    def getlist(cls):
        rawlist = requests.get('https://icanhazdadjoke.com/search', headers={"Accept": "application/json"})
        list = rawlist.json()
        print(list)
        endlist = list['results']
        return endlist


# ==========================================================
# count how many jokes retrieved
    @classmethod
    def getlistcount(cls):
        rawlist = requests.get('https://icanhazdadjoke.com', headers={"Accept": "application/json"})
        list = rawlist.json()
        print(list)
        endlist = list['total_jokes']
        return endlist


# ==========================================================
# parse through jokes using keyword
    @classmethod
    def searching(cls, data):
        rawlist = requests.get(f'https://icanhazdadjoke.com/search?term={data}', headers={"Accept": "application/json"})
        list = rawlist.json()
        print(list)
        endlist = list['results']
        return endlist


# ==========================================================
# count how many jokes are recieved with the parse
    @classmethod
    def counting(cls, data):
        rawlist = requests.get(f'https://icanhazdadjoke.com/search?term={data}', headers={"Accept": "application/json"})
        list = rawlist.json()
        print(list)
        endlist = list['total_jokes']
        return endlist