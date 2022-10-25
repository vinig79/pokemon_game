from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def app():
    app = Flask(__name__)
    app.config.from_object('config.Config')




    db.init_app(app)

    from index.routes import index_bp
    app.register_blueprint(index_bp)

    from login.login import login_bp
    app.register_blueprint(login_bp)

    with app.app_context():
        db.create_all()
        from sources.crawler import crawler
        crawler(db)

    return app


from model import *



if __name__ == "__main__":
    app().run(host="0.0.0.0", port=5000)
