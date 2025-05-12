from flask import request, redirect, url_for, render_template, Blueprint

login_bp = Blueprint('login_user',__file__)


@login_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Obtener los datos del formulario
        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]

        # Procesar datos (aquí podría ir validación de usuario, etc.)
        if usuario == "admin" and contraseña == "1234":
            return redirect(url_for('homePage', name=usuario))
        else:
            return "Datos incorrectos. Intenta de nuevo."

    return render_template("login.html")