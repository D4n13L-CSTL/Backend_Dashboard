from flask import Blueprint, request, jsonify
from .db import ajustes, detalles_de_ajustes

bp = Blueprint('ajustes', __name__, url_prefix='/ajustes')

@bp.route('api/v1/ajustes', methods=['POST'])
def index():
    try:
        data = request.json
        tienda = data.get('tienda')
        fecha_inicio = data.get('fecha_inicio') 
        fecha_fin = data.get('fecha_fin')
        
        if tienda:
            tienda = f'VAD10_{tienda}'
        
        valores = ajustes(tienda, fecha_inicio, fecha_fin)
        
        if valores == []:
            return jsonify({"message": "No se encontraron ajustes para el periodo especificado."}), 404

        return jsonify(valores), 200

    except Exception as e:
        return {"error": str(e)}, 500
    


@bp.route('api/v1/detalles', methods=['POST'])
def detalles():
    try:
        data = request.json
        tienda = data.get('tienda')
        if tienda:
            tienda = f'VAD10_{tienda}'
        fecha_inicio = data.get('fecha_inicio') 
        fecha_fin = data.get('fecha_fin')
        documento = data.get('documento')

        valores = detalles_de_ajustes(fecha_inicio, fecha_fin, tienda, documento)

        return jsonify(valores), 200

    except Exception as e:
        return {"error": str(e)}, 500
    

