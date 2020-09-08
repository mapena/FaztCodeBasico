from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
import json

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = 'myawesomesecretkey'

app.config['MONGO_URI'] = 'mongodb://localhost:27017/pythonmongodb'

mongo = PyMongo(app)
#----------------------------------------------------------------------------------
# parametros por url
@app.route('/param')
def leo_param():
    leoparam = request.args.get('parametro1','parametro1 inexistente')
    """
    http://127.0.0.1:3000/param?parametro1=marce -->  devuelve --> el parametro es marce
    http://127.0.0.1:3000/param -->  devuelve --> el parametro es parametro1 inexistente
    http://127.0.0.1:3000/param?parametro1=marce&parametro2=twity --> envia 2 parametros:
    parametro1=marce y parametro2=twity
    """
    return 'el parametro es {}'.format(leoparam)
#----------------------------------------------------------------------------------
@app.route('/argumentos')
@app.route('/argumentos/<nombre>')
@app.route('/argumentos/<nombre>/<int:numero>') # defino que el <int:numero> sea entero
def leo_argumentos(nombre = "ninguno",numero="nada"):
    """
    http://127.0.0.1:3000/argumentos/xx --> devuelve--> el argumento es es xx
    http://127.0.0.1:3000/argumentos --> devuelve--> el argumento es es ninguno
    http://127.0.0.1:3000/argumentos/hola --> devuelve --> el argumento es es hola nada
    http://127.0.0.1:3000/argumentos/hola/2332 --> devuelve --> el argumento es es hola 2332
    """
    return 'el argumento es es {} {}'.format(nombre,numero)
#------------------------------------------------------------------------------------------------
@app.route('/users', methods=['POST'])
def create_user():
    # Receiving Data
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if username and email and password: #pregunto si existe username y email y password
        
        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert(
            {'username': username, 'email': email, 'password': hashed_password})
        response = jsonify({
            '_id': str(id),
            'username': username,
            'password': password,
            'email': email
        })
        response.status_code = 201
        print("codigo de retorno 201")
        return response
    else:
        return not_found()


@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype="application/json")


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    print(id)
    user = mongo.db.users.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")


@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'User' + id + ' Deleted Successfully'})
    response.status_code = 200
    return response


@app.route('/users/<_id>', methods=['PUT'])
def update_user(_id):
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    if username and email and password and _id:
        hashed_password = generate_password_hash(password)
        mongo.db.users.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'username': username, 'email': email, 'password': hashed_password}})
        response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
        response.status_code = 200
        return response
    else:
      return not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(debug=True,port=3000)