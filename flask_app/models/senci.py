from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Senci:
    def __init__(self, data):
        self.id = data["id"]
        self.monto = data["monto"]

    @classmethod
    def save(cls, data):
        print("Guardando dato")
        print(data)
        query = "INSERT INTO senci (monto) VALUES (%(monto)s);"
        nuevoId = connectToMySQL('esquema_senci').query_db(query, data)
        return nuevoId