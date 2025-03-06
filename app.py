from flask import Flask

app = Flask(__name__) # instance of Flask

# from app import routes

@app.route("/")

def home():
    return "Hello World! ITS MEEEEE!!!! <3"