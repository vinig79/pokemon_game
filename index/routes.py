from flask import Blueprint, render_template, flash, redirect
from forms import Login
from model import User
from pokemon import db

index_bp =  Blueprint("index",__name__)

@index_bp.route("/", methods=["GET","POST"])
@index_bp.route("/index", methods=["GET","POST"])
def index():
    form = Login()
    if form.validate_on_submit():
        u = User.query.filter_by(nome=form.nome.data).first()
        if u is None:
            flash("email or username incorrect")
            redirect('/index')
        flash(f'login requested for user {form.nome.data}')
        return redirect("/index")
    return render_template("login.html", title="login", form=form)
