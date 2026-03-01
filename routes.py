from app import app, db
from flask import render_template
import formularios
from models import Tarea
from flask import render_template, request, redirect, url_for, flash

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
                return render_template('sobrenosotros.html', 
                                       form = formulario,
                                       titulo = formulario.titulo.data)
        return render_template('sobrenosotros.html', form = formulario)
    
@app.route('/saludo')
def saludo():
        return 'Hola bienvenido a Taller Apps '
    
@app.route('/usuario/<nombre>')
def usuario(nombre):
        return f'Hola{nombre} bienvenido a Taller Apps '
@app.route("/tareas")
def listar_tareas():
    tareas = Tarea.query.all()
    return render_template("tareas.html", tareas=tareas)


@app.route("/tarea/<int:tarea_id>/editar", methods=["GET", "POST"])
def editar_tarea(tarea_id):
    tarea = Tarea.query.get_or_404(tarea_id)

    if request.method == "POST":
        tarea.titulo = request.form.get("titulo")
        # si tu modelo NO tiene descripcion, borra la siguiente línea
        tarea.descripcion = request.form.get("descripcion")

        db.session.commit()
        flash("Tarea actualizada correctamente")
        return redirect(url_for("listar_tareas"))

    return render_template("editar.html", tarea=tarea)