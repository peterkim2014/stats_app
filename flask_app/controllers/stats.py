from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.stat import Stat
from flask_app.config.mysqlconnection import MySQLConnection

@app.route("/")
def view_homepage():
    return render_template("base.html")