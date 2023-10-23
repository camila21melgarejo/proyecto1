from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hola soy un titulo h1</h1>"


