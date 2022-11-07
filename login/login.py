from flask import Blueprint, render_template, flash, redirect, request
from login.forms import Login
from model import User
from flask_login import logout_user, current_user, login_user
from werkzeug.urls import url_parse


login_bp =  Blueprint("login", __name__)

@login_bp.route("/", methods=["GET","POST"])
@login_bp.route("/login", methods=["GET", "POST"])
def index():
    if current_user.is_authenticated:
        redirect("/home")
    form = Login()
    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data).first()
        if u is None or not u.check_password(form.password.data):
            flash("email or password incorrect")
            return redirect('/login')
        login_user(u, remember=form.remember_me.data)
        flash(f'register requested for user {form.email.data}')

        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            next_page = "/home"
        return redirect(next_page)

    return render_template("login.html", title="login", form=form)

@login_bp.route("/logout")
def logout():
    logout_user()
    return redirect("/login")