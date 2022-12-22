from flask import render_template, redirect, session, request, flash
from flask_app import app

@app.route("/")
def index1():
	return render_template("index1.html")