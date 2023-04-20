from flask import Flask

app = Flask(__name__)

@app.route("/")
def start():
    return "Ola bem vindo como vai?"

@app.route('/produtos')
def produtos():
    return "Minha pagina de produtos"