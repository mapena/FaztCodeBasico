from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo

from bson import json_util
from bson.objectid import ObjectId
import json

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "mysecretkey"  # se crea para crear una session que lo utiliza flash para los mensajes.
app.config['MONGO_URI'] = 'mongodb://localhost:27017/pythonmongodb'

mongo = PyMongo(app)

@app.route('/users', methods=['POST'])
def create_user():
    # Receiving Data
    print(request.json)
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    if username and email and password:
        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert(
            {'username': username, 'email': email, 'password': hashed_password})
        response = jsonify({
            '_id': str(id),        # convierto el id de mongodb a string #
            'username': username,
            'password': hashed_password,
            'email': email
        })
        response.status_code = 201
        return response
    else:
        return not_found()


    return {'message': 'received'}

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    #response = jsonify(message)
    #response.status_code = 404
    return message

#---------------------------------------------------------------------------------------------------------
# main
#---------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(port=3000, debug=True)
