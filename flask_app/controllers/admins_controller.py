from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.senci import Senci
from flask_app.iot import COM_ESP32

# crear metodo en carpeta models (senci.py) para almacenar
# var fondo en la base de datos

@app.route("/")
def index():
	# fondo = COM_ESP32.getDatafromESP()
	# Senci.save_fondo(fondo)
	# guardar en la base de datos 
	return render_template("index.html")
