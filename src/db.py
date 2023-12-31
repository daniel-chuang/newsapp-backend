from numpy import *
from time import time
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from pprint import pprint
from pandas import pandas

db = SQLAlchemy()

class Articles(db.Model):
    """
    SQLAlchemy Class for Articles, following this format when retrieved

    {
    - id
    - url
    - genre
    - perceived (?)
    - primary_topic
    - secondary_topic
    - democrat_vote
    - republican_vote
    - classification
    - (future idea) have users_id be recorded when they submit an article
    }
    """

    __tablename__ = "Articles"
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=True)
    perceived = db.Column(db.Integer, nullable=False)
    primary_topic = db.Column(db.String, nullable=False)
    secondary_topic = db.Column(db.String, nullable=True)
    democrat_vote = db.Column(db.String, nullable=False)
    republican_vote = db.Column(db.String, nullable=False)
    classification = db.Column(db.String, nullable=False)

class Users(db.Model):
    """
    SQLAlchemy Class for Users, following this format when retrieved

    {
    - id
    - username
    - password
    }
    """

    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)

class Ratings(db.Model):
    """
    SQLAlchemy Class for Ratings, following this format when retrieved

    {
    - id
    - article_id (foreign key to Articles)
    - user_id (foreign key to user)
    - rating
    }
    """

    __tablename__ = "Ratings"
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.ForeignKey("Articles.id"), primary_key=True)
    user_id = db.Column(db.ForeignKey("Users.id"), primary_key=True)
    rating = db.Column(db.Integer, nullable = False)