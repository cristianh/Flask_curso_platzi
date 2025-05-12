from flask import render_template, request, redirect, url_for, Blueprint, flash, session

from models.User import User,db


users_bp = Blueprint('users',__file__, url_prefix='/users')

@users_bp.route('/<nombre>')
@users_bp.route('/<nombre>/id/<int:id>')
@users_bp.route('/id/<int:id>')
def users(nombre="Invitado", id=1):
    find_user= User.query.get_or_404(id)
    return render_template("index.html", name=find_user)

@users_bp.route('/update/<int:id>', methods=["GET","POST"])
def udpdate_user(id):
    user = User.query.get_or_404(id)

    if request.method == "POST":
        session.pop('_flashes', None)
        # Obtener los datos del formulario
        nombre = request.form.get("nombre")
        materia = request.form.get("materia")
        nota = request.form.get("nota")
        user.nombre = nombre
        user.materia = materia
        user.nota = nota

        db.session.commit()
        flash("Registro Actualizado","info")
        #usuarios.append(newUsuario)

        return redirect(url_for('dashboard_user.dashboard', role="admin"))


    return render_template("updatenotas.html",user=user)


@users_bp.route('/<int:id>',methods=["POST","DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    #mensaje = f"Usuario con id {{id}}, eliminado"
    #return jsonify({"message": "Usuario eliminado"})
    flash("Usuario eliminado","danger")
    return redirect(url_for('dashboard_user.dashboard', role="admin"))