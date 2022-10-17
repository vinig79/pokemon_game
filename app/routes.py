from flask import render_template
from app import app
from app.forms import LoginForm
import requests
from random import randint

@app.route('/')
@app.route('/index')
def index():

    def retorno():
        request_pokemon = requests.get('http://pokeapi.co/api/v2/pokemon/')
        pokemons = request_pokemon.json()['results']
        pokemon = requests.get(pokemons[randint(0, len(pokemons))]['url']).json()['sprites']['back_default']
        return pokemon

    return render_template('index.html', title="Pokemon Game",imagem=retorno())

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title="login", form=form)