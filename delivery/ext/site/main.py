from flask import render_template
from flask import Blueprint


bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    return render_template("index.html", name="Douglas", items=["Celular", "Kindle", "Garrafa"])

@bp.route("/sobre")
def about():
    return render_template("about.html")

@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")

@bp.route("/teste")
def teste():
    return render_template("teste.vue")