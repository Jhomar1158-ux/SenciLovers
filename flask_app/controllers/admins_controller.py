from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.iot import COM_ESP32

@app.route("/")
def index():
	# Recibir MONTO
	# COM_ESP32.sendDataToESP32(dataESP)
	return render_template("index.html")