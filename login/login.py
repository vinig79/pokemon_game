from flask import Blueprint, render_template,flash, redirect
from forms import Register
from model import User
from pokemon import db

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=["GET","POST"])
def login():
    form = Register()
    if form.validate_on_submit():
        u = User(nome=form.nome.data,email=form.email.data)
        db.session.add(u)
        db.session.commit()
        flash(":)")
        return redirect('/index')

    return render_template("register.html",title="login", form=form)