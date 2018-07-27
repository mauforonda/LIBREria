from config.config import env
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random
import uuid
app = env['APP']
app.config['SQLALCHEMY_DATABASE_URI'] = env['SQL_CONF']['DB_URI']
db = SQLAlchemy(app)

def id_generator(size=150, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class Libro(db.Model):
    __tablename__ = 'libro'
    id = db.Column(db.Integer, primary_key=True)
    nombre_libro = db.Column(db.String(255), nullable=False)
    nombre_archivo = db.Column(db.Text, unique=True, nullable=False)
    autor = db.Column(db.String(120), nullable=False)
    genero = db.Column(db.String(255), nullable=True)
    imagen = db.Column(db.Text, nullable=True)
    likes = db.Column(db.Integer, nullable=False, default=0)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ## Define back relation with Conversacion
    comentarios = db.relationship('Comentarios', backref="comentarios", lazy=True)
    ## Define back relation with Sesion
    # sesion = db.relationship('Sesion', backref="sesion", lazy=True)

class Comentarios(db.Model):
    __tablename__ = 'comentarios'
    id = db.Column(db.Integer, primary_key=True)
    libro_id = db.Column(db.Integer, db.ForeignKey('libro.id'), nullable=False)
    comentario = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ## Define back relation with Conversacion
    # comentarios = db.relationship('Comentarios', backref="comentarios", lazy=True)
    ## Define back relation with Sesion
    # sesion = db.relationship('Sesion', backref="sesion", lazy=True)

db.create_all()
