from flask import render_template, Blueprint,flash, session
from models.User import User,db

dashboard_bp = Blueprint('dashboard_user',__file__)

@dashboard_bp.get('/dashboard/<string:role>')
def dashboard(role):
    # Obtener todos los registros
    usuarios = db.session.query(User).all()
    return render_template("dashboard.html", role=role,usuarios=usuarios)