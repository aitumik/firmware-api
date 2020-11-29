from flask import Blueprint, jsonify, request
from app import db

api = Blueprint('api', __name__)

@api.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return jsonify({'msg':'successfull'}),201
    return jsonify({'msg':'data'}),200

@api.route("/temp",methods=['GET','POST'])
def temp():
    data = {}
    return data

@api.route("/humidity",methods=['GET','POST'])
def humidity():
    data = {}
    return data





