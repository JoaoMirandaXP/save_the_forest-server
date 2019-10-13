from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'
app.run()
