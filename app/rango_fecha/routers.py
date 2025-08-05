from flask import Blueprint, jsonify, request
from datetime import datetime

from .db import llamada_de_funciones
from .db_2024 import llamada_de_funciones as llamada_de_funciones_2024



bp = Blueprint('rango_fecha', __name__, url_prefix='/fecha')

@bp.route('api', methods=['POST'])
def index():
    try:
        data = request.json
        fecha_init = data.get('fecha_init')
        fecha_end = data.get('fecha_end')
        
        if not fecha_init or not fecha_end:
            return jsonify({"error": "Both 'fecha_init' and 'fecha_end' are required"}), 400


        fecha_init_dt = datetime.strptime(fecha_init, "%Y-%m-%d")
        fecha_end_dt = datetime.strptime(fecha_end, "%Y-%m-%d")

        if fecha_init_dt.year < 2025 or fecha_end_dt.year < 2025:
            valores = llamada_de_funciones_2024(fecha_init, fecha_end)
        else:
            valores = llamada_de_funciones(fecha_init, fecha_end)

        return jsonify(valores)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

