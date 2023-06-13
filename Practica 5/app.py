from flask import Flask

app= Flask(__name__)

@app.route('/')

def cindex():
    return "Hola mundo Flask"

