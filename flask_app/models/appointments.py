from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime

from flask import flash 

class Appointments:

    def __init__(self, data):
        self.id = data['id']
        self.task = data['task']
        self.date = data['date']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, form):
        query = "INSERT INTO appointments (task, date, status, user_id) VALUES (%(task)s, %(date)s, %(status)s, %(user_id)s)"
        result = connectToMySQL('esquema_citas').query_db(query, form)
        return result
    
    @staticmethod
    def validate_appointment(form):
        is_valid = True

        if len(form['task']) < 3:
            flash('La tarea debe tener al menos 3 caracteres', 'appointment')
            is_valid = False
        
        if form['date'] == "":
            flash('Ingrese una fecha válida', 'appointment')
            is_valid = False
        
        return is_valid
    
    @classmethod
    def save(cls, form):
        query = "INSERT INTO appointments (task, date, status, user_id) VALUES (%(task)s, %(date)s, %(status)s, %(user_id)s)"
        result = connectToMySQL('esquema_citas').query_db(query, form)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT appointments.*, users.first_name FROM appointments JOIN users ON user_id = users.id"
        results = connectToMySQL('esquema_citas').query_db(query) 
        appointments = []
        for appointment in results:
            appointments.append(cls(appointment))
        return appointments
    
    @classmethod
    def get_by_id(cls, data):

        query = "SELECT appointments.*, users.first_name FROM appointments JOIN users ON user_id = users.id WHERE appointments.id = %(id)s" 
        result = connectToMySQL('esquema_citas').query_db(query, data)
        appointment = cls(result[0])
        return appointment
    
    @classmethod
    def update(cls, form):
        query = "UPDATE appointments SET task=%(task)s, date=%(date)s, status=%(status)s WHERE id = %(id)s"
        result = connectToMySQL('esquema_citas').query_db(query, form)
        return result
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM appointments WHERE id = %(id)s"
        result = connectToMySQL('esquema_citas').query_db(query, data)
        return result