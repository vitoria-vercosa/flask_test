from flask import Flask
from flask_cors import CORS,cross_origin
from flask import jsonify

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
@cross_origin()
def hello():
    return "Hello World!"


@app.route('/<name>/<int:age>/<gender>/')
@cross_origin()
def hello_name(name, age, gender):
    dic = {'name':name, 'age':age,'gender':gender}
    return jsonify(dic)
    #return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8897)
