from flask import Blueprint

index_bp = Blueprint("index", __name__)

@index_bp.route("/")
@index_bp.route("/index")
def index():
    return 'Well Come'