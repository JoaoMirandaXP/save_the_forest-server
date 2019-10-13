from flask import Flask

app = Flask(__name__)

@app.route('/info')
def hello():
    return '<h1>Hello, World!</h1>'
app.run(host='0.0.0.0',port=8080)
