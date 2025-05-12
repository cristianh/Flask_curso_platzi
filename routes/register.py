from flask import request, redirect, url_for, render_template, Blueprint, flash

from models.User import User,db

register_bp = Blueprint('register_user',__file__)


@register_bp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # Obtener los datos del formulario
        nombre = request.form.get("nombre")
        materia = request.form.get("materia")
        nota = request.form.get("nota")
        newUsuario = User(
            nombre= nombre, materia= materia, nota= nota
        )
        db.session.add(newUsuario)
        db.session.commit()
        flash("Registro Guardado","success")
        #usuarios.append(newUsuario)
        return redirect(url_for('dashboard_user.dashboard', role="admin"))

    return render_template("registronotas.html")