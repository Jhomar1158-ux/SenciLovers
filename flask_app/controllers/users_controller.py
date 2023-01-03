from flask import render_template, redirect, session, request, flash
from flask_app import app

@app.route("/step-1")
def step1():
	return render_template("step1.html")

@app.route("/step-2")
def step2():
	return render_template("step2.html")

@app.route("/step-3")
def step3():
	return render_template("step3.html")

@app.route("/finalizar-steps")
def finalizarSteps():
	return redirect("/retirar")

@app.route("/calculadora")
def calculadora():
	return redirect("/calculadora")
