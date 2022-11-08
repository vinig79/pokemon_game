from flask import Blueprint, render_template,redirect
from model import Pokemon
from pokemons.form import Favorite

pokemon_bp = Blueprint("pokemon", __name__)

@pokemon_bp.route("/pokemons", methods=["GET","POST"])
def pokemons():

    form = Favorite()
    pokemon = Pokemon.query.all()
    if form.validate_on_submit():
        print(form.set.data)
        print("oi")

    return render_template("pokemons.html",title="Pokemon", pokemon=pokemon, form=form)

