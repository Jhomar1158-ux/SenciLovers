from flask import render_template, redirect, session, request, flash
from flask_app import app


@app.route("/retirar")
def retirar():
	return render_template("retirar.html")