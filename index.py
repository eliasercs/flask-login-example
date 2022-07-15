from app import app
from utils.db import db

with app.app_context():
    db.create_all() # Crea todas las tablas en nuestra base de datos

if __name__ == "__main__":
    app.run(debug=True)