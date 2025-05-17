from config import Config
from flask import (
    Flask,
    render_template)

from routes.users import users_bp
from routes.register import register_bp
from auth.auth import login_bp
from routes.dashboard import dashboard_bp

from models.User import User, db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

#Register Rutas
app.register_blueprint(users_bp,)
app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(dashboard_bp)

@app.get('/home/<name>')
def home_page(name):
    return render_template("home.html", name=name)

if __name__ == "__main__":
    app.run(debug=True, port=5051)
