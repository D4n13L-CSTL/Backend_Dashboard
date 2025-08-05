from flask import Blueprint, jsonify, request
from collections import defaultdict
from .db import llamada, llamada_general
from datetime import datetime

bp = Blueprint('meses', __name__, url_prefix='/meses')



@bp.route('api/<tienda>', methods = ['GET'])
def meses_route(tienda):
    
    resumen_por_anio = defaultdict(lambda: {'V_BS': 0, 'V_USD': 0})
    if tienda == 'all':
        valores = llamada_general()
    else:
        valores = llamada(tienda)
        
    for item in valores:
        anio = datetime.strptime(item["FECHA"], "%Y-%m-%d").year
        resumen_por_anio[anio]['V_BS'] += item['V_BS']
        resumen_por_anio[anio]['V_USD'] += item['V_USD']

    
    return jsonify(resumen_por_anio)