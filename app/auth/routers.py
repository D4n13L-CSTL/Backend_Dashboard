from flask import Blueprint, request, jsonify
from .db import create_users, update_users, delete_users

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('api/create' , methods = ['POST'])
def auth_route():
    try:
        data = request.json
        nombre_apellido = data['nombre_apellido'].upper()
        username = data['username'].upper()
        password = data['password']
        email = data['email'].upper()
        cargo = data['cargo'].upper()
        create_users(nombre_apellido, username, password, email, cargo)
        return jsonify({'Mensaje':"Creado Exitosamente"})
    except Exception as e:
        return jsonify({'Error':str(e)}) ,500
    

@bp.route('api/update/<campo>/<id_users>', methods = ['PUT'])
def update_auth_route(campo,id_users):
    try:
        data = request.json
        
        valor = data['valor_nuevo']
        update_users(campo,valor, id_users )
        
        return jsonify({'Mensaje':"Actualizado Exitosamente"})
    except Exception as e:
        return jsonify({'Error':str(e)}) ,500
    


@bp.route('api/delete/<username>', methods = ['DELETE'])
def delete_auth_route(username):
    try:
        
        
        delete_users(username)
        
        return jsonify({'Mensaje':"Eliminado Exitosamente"})
    except Exception as e:
        return jsonify({'Error':str(e)}) ,500