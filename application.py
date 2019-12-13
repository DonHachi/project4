import os
import requests
from flask import Flask, session,render_template,flash, request, redirect, url_for
from flask_session import Session


app = Flask(__name__)

# Check for environment variable

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/manga")
def manga():
    return render_template("manga.html")
@app.route("/dc")
def dc():
    return render_template("dc.html")
@app.route("/marvel")
def marvel():
    return render_template("marvel.html")
