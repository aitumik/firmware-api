from datetime import datetime,timedelta
from flask import Blueprint,request,jsonify,render_template

from app.api.models import Data

main = Blueprint('main',__name__)

@main.route("/")
def index():
    data = [d.to_json() for d in Data.query.all()]
    return render_template("index.html",data=data)

@main.route("/humidity")
def humidity():
    data = [d.to_json() for d in Data.query.all()]
    return render_template("humidity.html",data=data)

@main.route("/pastdata/<minutes>",methods=['GET','POST'])
def past_data(minutes):
    offset = datetime.now() - timedelta(minutes=int(minutes))
    data = Data.query.all()
    data = [d for d in data if d.timestamp < offset]
    return render_template("previous_data.html",data=data)

@main.route("/test")
def test():
    return render_template("test.html")

