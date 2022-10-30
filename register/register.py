from flask import Blueprint, render_template,flash, redirect
from register.forms import Register
from model import User
from pokemon import db

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=["GET", "POST"])
def login():
    form = Register()
    if form.validate_on_submit():
        u = User(nome=form.nome.data,email=form.email.data)
        u.set_password(form.password_1.data)
        db.session.add(u)
        db.session.commit()
        flash(":)")
        return redirect('/login')

    return render_template("register.html",title="register", form=form)