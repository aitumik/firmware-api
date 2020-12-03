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

@main.route("/pastdata/humidity/<minutes>",methods=['GET','POST'])
def past_humid(minutes):
    offset = datetime.now() - timedelta(minutes=int(minutes))
    data = Data.query.all()
    data = [d for d in data if d.timestamp < offset]
    if len(data) > 50:
        data = data[len(data) - 50:len(data)]

    labels = [str(j.timestamp).split(" ")[1].split(".")[0] for j in data]
    values = [j.humidity for j in data]

    colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

    return render_template("previous_data.html",title="Previous \
            Humidity Data",max=100,labels=labels,values=values)

@main.route("/pastdata/temperature/<minutes>",methods=['GET','POST'])
def past_temp(minutes):
    offset = datetime.now() - timedelta(minutes=int(minutes))
    data = Data.query.all()
    data = [d for d in data if d.timestamp < offset]
    if len(data) > 50:
        data = data[len(data) - 50:len(data)]

    labels = [str(j.timestamp).split(" ")[1].split(".")[0] for j in data]
    values = [j.temperature for j in data]

    colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

    return render_template("previous_temperature.html",title="Previous \
            Temperature Data",max=60,labels=labels,values=values)

@main.route("/test")
def test():
    return render_template("test.html")
