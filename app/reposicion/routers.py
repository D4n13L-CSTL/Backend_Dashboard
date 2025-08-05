from flask import Blueprint, request, jsonify
from .db import reposicion

bp = Blueprint('reposicion', __name__, url_prefix='/reposicion')

@bp.route('api/v1' ,methods=['POST'])
def index():
    try:
        data = request.json
        codigo = data.get('codigo')
        fecha_inicio = data.get('fecha_inicio')
        fecha_fin = data.get('fecha_fin')

        resultados = reposicion(codigo, fecha_inicio, fecha_fin)
        return jsonify(resultados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500                     