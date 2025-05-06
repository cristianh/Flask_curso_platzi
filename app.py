from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#Configurando BD
DB_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    "notes.sqlite"
)

# Configuración de SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_FILE_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de usuario
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    materia = db.Column(db.String(120), nullable=False)
    nota = db.Column(db.Integer, nullable=False)

"""usuarios = [
    {"nombre": "Juan", "materia": "fisica", "nota": 4.1},
    {"nombre": "Cristian", "materia": "quimica", "nota": 5},
    {"nombre": "Camilo", "materia": "fisica", "nota": 3.0},
    {"nombre": "Andres", "materia": "quimica", "nota": 1}
]"""

@app.get('/')
def home():
    return 'Hola mundo'


@app.get('/demo')
def demoFlask():
    return 'Hola demo'


@app.get('/dashboard/<string:role>')
def dashboard(role):
    # Obtener todos los registros
    usuarios = db.session.query(User).all()
    return render_template("dashboard.html", role=role,usuarios=usuarios)


@app.get('/home/<name>')
def homePage(name):
    return render_template("home.html", name=name)


@app.route('/login', methods=["GET", "POST"])
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


@app.route('/register', methods=["GET", "POST"])
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
        #usuarios.append(newUsuario)
        return redirect(url_for('dashboard', role="admin"))

    return render_template("registronotas.html")

@app.route('/users/<nombre>')
@app.route('/users/<nombre>/id/<int:id>')
@app.route('/users/id/<int:id>')
def users(nombre="Invitado", id=1):
    find_user= User.query.get_or_404(id)
    return render_template("index.html", name=find_user)

@app.route('/users/update/<int:id>', methods=["GET","POST"])
def udpdate_user(id):
    user = User.query.get_or_404(id)

    if request.method == "POST":
        # Obtener los datos del formulario
        nombre = request.form.get("nombre")
        materia = request.form.get("materia")
        nota = request.form.get("nota")
        user.nombre = nombre
        user.materia = materia
        user.nota = nota

        db.session.commit()
        #usuarios.append(newUsuario)
        return redirect(url_for('dashboard', role="admin"))

    return render_template("updatenotas.html",user=user)


@app.route('/users/<int:id>',methods=["POST","DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    mensaje = f"Usuario con id {{id}}, eliminado"
    #return jsonify({"message": "Usuario eliminado"})
    return redirect(url_for('dashboard', role="admin",mensaje=mensaje))





if __name__ == "__main__":
    app.run(debug=True, port=5051)
