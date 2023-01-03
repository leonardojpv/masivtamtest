from flask import Flask, render_template, request, redirect, url_for, json
import os
from classes.MySQLConnector import MySQLConnector
from classes.user import User

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)
db = MySQLConnector()

#Rutas de la aplicación
@app.route('/')
def home():
    data = User().getAll()
    return render_template('index.html', data = data)

#Ruta para guardar usuarios en la bdd
@app.route('/addUser', methods=['POST'])
def addUser():
    user = User(request.form['name'], request.form['age'], request.form['username'], request.form['email'])
    user.saveToDB();
    return redirect(url_for('home'))

@app.route('/deleteUser/<string:id>')
def deleteUser(id):
    User().deleteFromDB(id)
    return redirect(url_for('home'))

@app.route('/editUser/<string:id>', methods=['POST'])
def editUser(id):
    user = User(request.form['name'], request.form['age'], request.form['username'], request.form['email'])
    user.updateDB(id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)