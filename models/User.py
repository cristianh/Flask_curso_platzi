from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    materia = db.Column(db.String(120), nullable=False)
    nota = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return {"id": self.id, "nombre": self.nombre, "materia": self.materia, "nota": self.nota}
