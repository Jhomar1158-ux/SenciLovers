from flask import render_template, redirect, session, request, flash
from flask_app import app
import json
from flask_app.models.senci import Senci

@app.route('/retiro-monto', methods=['POST'])
def test():
	output = request.get_json()
	result = json.loads(output) #json -> diccionario
	print(result)
	Senci.save(result)

@app.route("/loader")
def loader():
	return render_template("loader.html")


@app.route('/confirmar-retiro')
def confirmarRetiro():
	monto = Senci.getMonto()
	montoActual = monto[0]['monto']
	print("Monto más reciente")
	print(montoActual)
	return render_template("confirmar_retiro.html", montoActual=montoActual)

@app.route("/retirar")
def retirar():
	return render_template("retirar.html")


@app.route("/retirar-otro")
def retirarOtro():
	return render_template("retirar_otro.html")