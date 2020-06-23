from flask import Flask
from flask_cors import CORS,cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
@cross_origin()
def hello():
    return "Hello World!"


@app.route('/<name>')
@cross_origin()
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005)
