from flask import Blueprint, request, jsonify
from .db import union_de_funciones, ventas_por_departamento,ventas_por_tendencias
from .db_controller import union_de_funciones_ultimo_update
from collections import defaultdict


bp = Blueprint('api_agentes', __name__, url_prefix='/agentes')


@bp.route('api/<tienda>', methods=['GET', 'POST'])
def index(tienda):
    try:
        data = request.json
        fecha_inicio = data.get("FechaInicio")
        fecha_fin = data.get("FechaFin")
        valores = union_de_funciones(fecha_inicio, fecha_fin, tienda)
        return jsonify(valores)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('api/update/<tienda>/<server>', methods=['GET', 'POST'])
def update_ultimo_valor_for_day_route(tienda,server):
    try:
        data = request.json
        fecha_inicio = data.get("FechaInicio")
        fecha_fin = data.get("FechaFin")
        valores = union_de_funciones_ultimo_update(fecha_inicio, fecha_fin, tienda,server)
        return jsonify(valores)
    except Exception as e:
        return jsonify({"error": str(e)}), 500






@bp.route('api/departamentos', methods=['GET', 'POST'])
def ventas_Departamentos_routes():
    try:
        data = request.json
        fecha_inicio = data.get("FechaInicio")
        fecha_fin = data.get("FechaFin")
    
        valores = ventas_por_departamento(fecha_inicio, fecha_fin)
        

        return jsonify(valores)
    except Exception as e:
        return jsonify({"error": str(e)}), 500




@bp.route('api/tendencias', methods=['POST'])
def tendecias_agents_route():
    data = request.json
    fecha_inicio = data.get("FechaInicio")
    fecha_fin = data.get("FechaFin")
    
    valores = ventas_por_tendencias(fecha_inicio, fecha_fin)

    
    return jsonify(valores)


