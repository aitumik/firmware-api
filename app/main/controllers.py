from flask import Blueprint,request,jsonify,render_template

from app.api.models import Data

main = Blueprint('main',__name__)

@main.route("/")
def index():
    data = [d.to_json() for d in Data.query.all()[:100]]
    return render_template("index.html",data=data)

@main.route("/test")
def test():
    return render_template("test.html")
