from flask import Blueprint

index_bp =  Blueprint("index",__name__)

@index_bp.route("/", methods=["GET"])
@index_bp.route("/index", methods=["GET"])
def index():
    return "Olá, Mundo!"
