from flask import Blueprint, render_template,flash
from model import Pokemon
from pokemon import db
from pokemons.form import Favorite
from flask_login import current_user

pokemon_bp = Blueprint("pokemon", __name__)

@pokemon_bp.route("/pokemons", methods=["GET","POST"])
def pokemons():

    form = Favorite()
    pokemon = Pokemon.query.all()


    return render_template("pokemons.html",title="Pokemon", pokemon=pokemon, form=form)

@pokemon_bp.route("/pokemon/<nome>", methods=["GET","POST"])
def pokemon(nome):
    form = Favorite()
    user = current_user
    pok = Pokemon.query.filter_by(nome=nome).first_or_404()
    print("i")
    if form.is_submitted():
        print("l")
        if user.is_favorite(pok):
            user.favoritar(pok)
            db.session.commit()
            flash("Favoritado")
        else:
            user.desfavoritar(pok)
            print("ei")
            db.session.commit()
            flash("Desfavoritado")
    return render_template("pokemon.html", pok=pok, user=user, form=form)

@pokemon_bp.route("/favorito",methods=["GET","POST"])
def favorito():
    user = current_user
    return render_template("favorito.html",user=user)