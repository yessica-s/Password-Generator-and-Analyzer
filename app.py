from flask import Flask, request, jsonify
from password_generator import PasswordGenerator

app = Flask(__name__) # instance of Flask

# from app import routes

@app.route("/")

def home():
    return "Hello World!"

@app.route("/generate", methods=["GET"])

def generate():
    length = int(request.args.get('length'))
    uppercase = request.args.get('uppercase', 'false').lower() == 'true'
    numbers = request.args.get('numbers', 'false').lower() == 'true'
    symbols = request.args.get('symbols', 'false').lower() == 'true'

    password = PasswordGenerator.generate_password(length, uppercase, numbers, symbols) # call password generation function
    return jsonify({"password": password}) # return password as JSON data

