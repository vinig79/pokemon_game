from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()

def app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    login.init_app(app)
    login.login_view = "/login"


    db.init_app(app)

    from login.login import login_bp
    app.register_blueprint(login_bp)

    from register.register import register_bp
    app.register_blueprint(register_bp)

   #from index.index import index_bp
    #app.register_blueprint(index_bp)

    from home.home import home_bp
    app.register_blueprint(home_bp)


    with app.app_context():
        db.create_all()
        from sources.crawler import crawler
        crawler(db)

    return app


from model import *



if __name__ == "__main__":
    app().run(host="0.0.0.0", port=5000)
