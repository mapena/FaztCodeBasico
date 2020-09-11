from flask import Flask, request, Response # Response para devolver al cliente un mensaje
from flask import jsonify  #para manejar mejor el codigo de retorno del servidor al cliente por ejemplo ver response.status.code =404
from flask_pymongo import PyMongo
from bson import json_util  #para convertir los formatos bson (que usa mongodb) a json
from bson.objectid import ObjectId # sirve para convertir un objeto str a objeto mongodb
import json

from werkzeug.security import generate_password_hash, check_password_hash

#---------------------------------
#---------------------------------
import os

os.system("")

# Group of Different functions for different styles
class style():
    RED = '\033[31m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.RED + "Hello, World!")
print(style.RESET + "Hello, World!")
#---------------------------------
#---------------------------------

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
@app.route('/users', methods=['POST']) # con post es para recibir el servidor
def create_user():
    # Receiving Data
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if username and email and password: #pregunto si existe username y email y password
        
        hashed_password = generate_password_hash(password)
        # mongodb cuando inserta genera un id (mongodb trabaja formato json)
        id = mongo.db.users.insert({'username': username, 'email': email, 'password': hashed_password})
        
        response = jsonify({
            '_id': str(id),       ## id es de formato objectID x eso lo convierto a str
            'username': username,
            'password': password,
            'email': email
        })
        response.status_code = 201
        print("codigo de retorno 201")
        return response
    else:
        return not_found()


@app.route('/users', methods=['GET'])  # cunado se le piede info al servidor
def get_users():
    users = mongo.db.users.find() # mongodb guarda los datos en formato bson,
    """
     users queda de tipo ==> 'pymongo.cursor.Cursor'  (bson)
     para manipular mejor los datos se convertira la variable "users" a formato json
     para eso usamos la libreria json_util.dumps

    """
    response = json_util.dumps(users) # response quedo en formato json
    """
    para responder usaremos el objeto Response >>(from flask import  Response)
    donde indicamos que la respuesta es de formato json (application/json)
    asi recive el cliente:
     {
        "_id": {
            "$oid": "5f56a4ee4d459dbf3d029e03"   ==> Object_id de mongodb
        },
        "username": "Fazt",
        "email": "xx@gmail.com",
        "password": "pbkdf2:sha256:150000$iMvpRMZy$e84caedf578beaac1f0a91159ce5acd11f0574f1969123c803c847fed2adc0be"
    }
    """
    return Response(response, mimetype="application/json")


@app.route('/users/<id>', methods=['GET']) # se le pasa por parametro en <id> el objectID de mongodb
def get_user(id):
    print(id)
    # la variable id la debo convertir a formato $oid de mongodb
    user = mongo.db.users.find_one({'_id': ObjectId(id), })  # find_one me trae un registro, si hay mas de uno, solo trae el primero
    #user quedo en formato bson y con json_util.dumos lo convierto a json
    response = json_util.dumps(user)
    # si return response devolveria con formato str , como quiero responder en formato json uso el Response
    # indicamos que la respuesta es de formato json (application/json)
    return Response(response, mimetype="application/json")
 

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'User' + id + ' Deleted Successfully'})
    response.status_code = 200
    return response

# peticiones http => put,get,delete,post
@app.route('/users/<_id>', methods=['PUT']) #para actualizar tambien se usa el metodo PATH, que se usa para actualizar 1 solo dato
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


@app.errorhandler(404)  #manejador de errores
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    # a continuacion se guarda el message en un objeto json hace que se pueda usar mas propiedades del obj. como
    # por ejemplo .status.code = 404
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(debug=True,port=3000)