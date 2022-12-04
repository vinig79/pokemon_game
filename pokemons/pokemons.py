from flask import Blueprint, render_template,redirect
from model import Pokemon
from pokemons.form import Favorite

pokemon_bp = Blueprint("pokemon", __name__)

@pokemon_bp.route("/pokemons", methods=["GET","POST"])
def pokemons():

    form = Favorite()
    pokemon = Pokemon.query.all()


    return render_template("pokemons.html",title="Pokemon", pokemon=pokemon, form=form)

@pokemon_bp.route("/pokemon/<nome>", methods=["GET","POST"])
def pokemon(nome):
    pok = Pokemon.query.filter_by(nome=nome).first_or_404()
    return render_template("pokemon.html", pok=pok)
