from flask import Blueprint, render_template, flash, redirect
from forms import Login

index_bp =  Blueprint("index",__name__)

@index_bp.route("/", methods=["GET"])
@index_bp.route("/index", methods=["GET"])
def index():
    form = Login()
    if form.validate_on_submit():
        flash(f'login requested for user {form.nome.data}')
        return redirect("/routes")
    return render_template("login.html",title="login", form=form)
