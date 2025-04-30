import sys
import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from services.db import get_db_connection
from models.models import Usuario

# Configuración de Flask
app = Flask(__name__,
            template_folder='../../frontend/templates',
            static_folder='../../frontend/static')
app.secret_key = 'supersecretkey'  # Asegúrate de tener una clave secreta para sesiones

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Cargar el usuario
@login_manager.user_loader
def load_user(user_id):
    return Usuario.get_by_id(user_id)

# Obtener motos
def obtener_motos():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM motos')
    motos = cursor.fetchall()
    connection.close()
    return motos

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/motos')
def motos():
    motos_data = obtener_motos()
    return render_template('motos.html', motos=motos_data)

# Login corregido sin .query
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        # Consultar usuario directamente desde la base de datos
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
        user_data = cursor.fetchone()
        connection.close()

        if user_data and check_password_hash(user_data['contraseña'], contraseña):
            user = Usuario(**user_data)  # Convertir dict a objeto Usuario
            login_user(user)
            session['rol'] = user.rol
            flash("Inicio de sesión exitoso", "success")
            if user.rol == 'admin':
                return redirect(url_for('agregar_moto'))
            else:
                return redirect(url_for('index'))
        else:
            flash("Correo o contraseña incorrectos", "danger")

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        hashed_password = generate_password_hash(contraseña)

        # Verificar si ya existe
        if Usuario.get_by_email(correo):
            flash('El correo ya está registrado.')
        else:
            Usuario.create(nombre, correo, hashed_password)
            flash('Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect(url_for('login'))

    return render_template('registro.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión con éxito.')
    return redirect(url_for('index'))

@app.route('/agregar_moto', methods=['GET', 'POST'])
@login_required
def agregar_moto():
    if current_user.rol != 'admin':
        flash('No tienes permiso para agregar motos.')
        return redirect(url_for('index'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        imagen_url = request.form['imagen_url']

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(''' 
            INSERT INTO motos (nombre, marca, modelo, precio, imagen_url)
            VALUES (%s, %s, %s, %s, %s)
        ''', (nombre, marca, modelo, precio, imagen_url))
        connection.commit()
        connection.close()

        flash('Moto agregada con éxito.')
        return redirect(url_for('motos'))

    return render_template('agregar_moto.html')

if __name__ == '__main__':
    app.run(debug=True)
