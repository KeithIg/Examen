from flask import Flask, render_template, redirect, session, request, flash
from flask_app import app

from flask_app.models.users import User
from flask_app.models.appointments import Appointments

@app.route('/date/new')
def date_new():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    return render_template('crear.html')

@app.route('/create/date', methods=['POST'])
def create_date():
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    if not Appointments.validate_appointment(request.form):
        return redirect('/date/new')
    Appointments.save(request.form)
    
    return redirect('/appointments')


@app.route('/appointments/edit/<int:id>')
def cita_edit(id):
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    diccionario = {"id": id}
    appointment = Appointments.get_by_id(diccionario)

    if appointment.user_id != session['user_id']:
        return redirect('/dashboard')

    return render_template('editar.html', appointment=appointment)

@app.route('/appointments/update', methods=['POST'])
def cita_update():
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    if not Appointments.validate_appointment(request.form):
        return redirect('/appointments/edit/' +request.form['id'])
    
    Appointments.update(request.form)
    return redirect('/dashboard')

@app.route('/appointments/delete/<int:id>')
def recipes_delete(id):
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    diccionario = {"id": id}
    Appointments.delete(diccionario)
    return redirect('/appointments')