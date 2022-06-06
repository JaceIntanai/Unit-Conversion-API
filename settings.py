from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
import base64

app = Flask(__name__)
auth = HTTPBasicAuth()

USER_DATA = {
    "jace" : "pwdintanai"
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False