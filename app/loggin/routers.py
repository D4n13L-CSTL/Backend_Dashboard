from flask import Blueprint, jsonify, request
from .db import loggin_ps
import bcrypt
from ..alert_bot.alert import enviar_mensaje

bp = Blueprint('loggin', __name__, url_prefix='/loggin')

@bp.route('api' ,methods = ['POST'])
def indexv3():
    try:
        data = request.json
        usuario = data['usuario'].upper()
        password = data['password']

        if usuario:
            respuesta = loggin_ps(usuario)
            if not respuesta:
                return jsonify({"Respuesta": "Usuario no encontrado"}), 404

            password_hasheada = respuesta[0][2]

            if password_hasheada and bcrypt.checkpw(password.encode('utf-8'), password_hasheada.encode('utf-8')):
                # enviar_mensaje(f'El usuario {usuario} ha iniciado sesion')
                return jsonify({"Respuesta": True}), 200
            else:
                return jsonify({"Respuesta": "Contraseña incorrecta"}), 401

    except Exception as e:
        return jsonify({'Error': str(e)}), 500

