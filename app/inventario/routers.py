from flask import Blueprint, request, jsonify
from .db import inventario_movimiento

bp = Blueprint('inventario', __name__, url_prefix='/inventario')

@bp.route('/api/v1', methods=['POST'])
def api_v1():
    try:
        data = request.json
        deposito = data.get('deposito')
        fecha_inicio = data.get('fecha_inicio')
        base_datos = data.get('base_datos')
        departamento = data.get('departamento')

        resultados = inventario_movimiento(deposito, fecha_inicio, base_datos, departamento)
        
        return jsonify(resultados), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
