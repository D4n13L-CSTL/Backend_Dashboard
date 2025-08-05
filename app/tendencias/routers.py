from flask import Blueprint, jsonify
from .db import retorno_serializado, cantidades
from collections import defaultdict
from .meses import mes_fin, mes_init
from datetime import datetime, timedelta


fecha = datetime.now()
mes_date = fecha.date().month
indice_de_mes = mes_date - 1

bp = Blueprint('tendencias', __name__, url_prefix='/tendencias')



@bp.route('api/v1/<dpto>', methods=['POST'])
def index_routes(dpto):
    fechaini = mes_init[indice_de_mes]
    fechFin = mes_fin[indice_de_mes]
    resultado = retorno_serializado(fechaini,fechFin,dpto)
    return jsonify(resultado)




@bp.route('api/cantidad/v1', methods=['GET'])
def cantidad_routes():
    dptos = ['AC','AU','BE','CI','CO','CP','CZ','DP','FE','FR','HG','IN','JG','OF','PE','PL','RP','TG']
        
    valores = cantidades(mes_init[indice_de_mes],mes_fin[indice_de_mes])
    
    parcial = {item['deptos']: float(item['sum']) for item in valores}
    
    final = {d: parcial.get(d, 0.0) for d in dptos}

    return jsonify(final)

