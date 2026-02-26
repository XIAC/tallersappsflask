from app import app, db
from flask import render_template, redirect, url_for, request
import formularios
from models import Tarea

@app.route('/')
@app.route('/index')
def index():
        return render_template('index.html', subtitulo = "Actidad en grupo TAI")

@app.route('/sobrenosotros', methods = ['GET', 'POST'])
def sobrenosotros():
        formulario = formularios.FormAgregarTareas()
        if formulario.validate_on_submit() :
                nueva_tarea = Tarea (titulo =  formulario.titulo.data)
                db.session.add(nueva_tarea)
                db.session.commit()
                print('se envio correctamente', formulario.titulo.data)
        
        tareas = Tarea.query.all()
        return render_template('sobrenosotros.html', 
                               form = formulario,
                               tareas = tareas)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
        tarea = Tarea.query.get_or_404(id)
        form = formularios.FormAgregarTareas(obj=tarea)

        if form.validate_on_submit():
                tarea.titulo = form.titulo.data
                db.session.commit()
                return redirect(url_for('sobrenosotros'))
        return render_template('editar.html', form = form)

@app.route('/saludo')
def saludo():
        return 'Hola bienvenido a Taller Apps '
    
@app.route('/usuario/<nombre>')
def usuario(nombre):
        return f'Hola{nombre} bienvenido a Taller Apps '
