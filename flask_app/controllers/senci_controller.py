from flask import render_template, redirect, session, request, flash
from flask_app import app
import json

@app.route('/retiro-monto', methods=['POST'])
def test():
    output = request.get_json()
    result = json.loads(output) #json -> diccionario
    print(result)
    return result

@app.route("/retirar")
def retirar():
	return render_template("retirar.html")


@app.route("/retirar-otro")
def retirarOtro():
	return render_template("retirar_otro.html")