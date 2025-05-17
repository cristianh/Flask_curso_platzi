from flask import request, redirect, url_for, render_template, Blueprint, session, flash

login_bp = Blueprint('login_user',__file__)


@login_bp.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Obtener los datos del formulario
        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]

        # Procesar datos (aquí podría ir validación de usuario, etc.)
        if usuario == "admin" and contraseña == "1234":
            session["user"]=usuario
            return redirect(url_for('dashboard_user.dashboard', role=usuario))
        else:
            flash("Datos incorrectos. Intenta de nuevo.","danger")
            return redirect(url_for('login_user.login'))
    return render_template("login.html")


@login_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash("la sesion se ha cerrado correctamente","info")
    return render_template("login.html")