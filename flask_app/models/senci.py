from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Senci:
    def __init__(self, data):
        self.monto = data["monto"]
        self.created_at= data["created_at"]
        self.updated_at=data["updated_at"]

    @classmethod
    def save(cls, data):
        print("Guardando dato")
        print(data)
        query = "INSERT INTO senci (monto) VALUES (%(monto)s);"
        nuevoId = connectToMySQL('esquema_senci').query_db(query, data)
        return nuevoId

    @classmethod
    def getMonto(cls):
        query = "SELECT monto FROM senci ORDER BY senci.created_at DESC;"
        results = connectToMySQL('esquema_senci').query_db(query)
        return results