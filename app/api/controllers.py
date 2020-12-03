from datetime import datetime,timedelta
from flask import Blueprint, jsonify, request
from app import db
from .models import Data

api = Blueprint('api', __name__)

@api.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return jsonify({'msg':'successfull'}),201
    return jsonify({'msg':'data'}),200

@api.route("/data",methods=['GET','POST'])
def data():
    if request.method == 'POST':
        temp = request.json.get('temp')
        humidity = request.json.get('humidity')
        d = Data(temperature=temp,humidity=humidity)
        d.save()
        return jsonify({'msg':'data posted successfully'}),201
    count = Data.query.count();
    res = [i.to_json() for i in Data.query.all()[::][count - 50:count]]
    return jsonify({'msg':res}),200

@api.route("/prev-data/<int:minutes>",methods=['GET'])
def prev_data(minutes):
    past_time = datetime.now() - timedelta(minutes=int(minutes))
    d = Data.query.filter_by(timestamp=past_time).all()
    
    if len(d) > 50:
        d = d[:50]
    res = [i.to_json() for i in d]
    return jsonify({'msg':res}),200


