from flask import Blueprint, render_template
from model import Pokemon

pokemon_bp = Blueprint("pokemon", __name__)

@pokemon_bp.route("/pokemons")
def pokemons():
    pokemon = Pokemon.query.all()
    return render_template("pokemons.html",title="Pokemon", pokemon=pokemon)

