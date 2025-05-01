from flask import Flask, render_template, request #el request es un metodo
import requests #aca importo la libreria completa
from datetime import date


app = Flask(__name__) #__main__ tmb deberia ser lo mismo, es para inicializar la app del enviroment 

@app.context_processor
def get_current_year():
    return {
        'current_year': date.today().year,
        'today': date.today()
    }



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacto/<nombre>')
def contacto(nombre):
    data={
        'titulo':'Contacto',    
        'nombre':nombre
    }
    return render_template(contacto.html, data=data)

@app.route('/users/')
def users():
    cant = request.args.get('cant', 9, int)
    response = requests.get(
        f'https://randomuser.me/api/?results={cant}').json()
    usuarios=response['results']
    return render_template(
        'users.html',
        usuarios=usuarios
        )   