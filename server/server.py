from flask import Flask

app = Flask(__name__)

@app.route('/info')
def hello():
    return '<h1>Info deve aparecer abaixo</h1><br><h3>Temp.</h3><br><h3>Co2</h3><br><h3>Hum.</h3>'
app.run(host='0.0.0.0',port=8080)


