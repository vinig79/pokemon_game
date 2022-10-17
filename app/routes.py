from flask import render_template, request
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
def home():
    return "Hello, Pokemon!"

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title="")