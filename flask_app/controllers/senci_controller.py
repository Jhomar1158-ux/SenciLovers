from flask import render_template, redirect, session, request, flash
from flask_app import app
import json
from flask_app.models.senci import Senci
from flask_app.iot import conversion_data
from flask_app.iot import COM_ESP32
@app.route('/retiro-monto', methods=['POST'])
def test():
	output = request.get_json()
	result = json.loads(output) #json -> diccionario
	print(result)
	#Crear una validación para retiros 0.1 a 0.4 y 0.6 a 0.9 antes de guardar en la db
	#retiro = result["monto"]
	#print("Validación")
	#print(retiro)
	#print("---")
	#flag = Senci.validation(retiro) #[True, retiroActualFloat] [False, retiroActualFloat]
	#if (flag[0]):
	print("Guardar dato en DB")
	Senci.save(result)
	print(result)

@app.route("/loader")
def loader():
	return render_template("loader.html")

@app.route('/confirmar-retiro')
def confirmarRetiro():
	monto = Senci.getMonto()
	retiroActual = monto[0]['monto']

	print("Monto más reciente")
	print(retiroActual)
	# Pasarela de pago
	fondo = COM_ESP32.getDatafromESP()
	# print(conversion_data.validation(float(retiroActual),fondo))
	if conversion_data.validation(float(retiroActual),fondo):
		return render_template("confirmar_retiro.html", retiroActual=retiroActual)
	return redirect("/")

@app.route("/confimado")
def confimado():
	monto = Senci.getMonto()
	retiroActual = monto[0]['monto']
	fondo = COM_ESP32.getDatafromESP()
	dataESP = conversion_data.convertir_monto(float(retiroActual),fondo)
	print(fondo)
	print(dataESP)
	print(type(dataESP))
	# 
	COM_ESP32.sendDataToESP32(dataESP)
	return redirect("/")

@app.route("/retirar")
def retirar():
	return render_template("retirar.html")


@app.route("/retirar-otro")
def retirarOtro():
	return render_template("retirar_otro.html")