from flask import Blueprint, jsonify, request
from .db import get_marcas_USD, get_marcas_BS
from collections import OrderedDict,defaultdict
from .tiendas import tiendas_completas, tiendas_simplificadas


bp = Blueprint('marcas', __name__, url_prefix='/marcas')

@bp.route('api', methods=['POST'])
def index():
    try:
        
        data = request.json
        fecha_inicio = data.get('fecha_inicio')
        fecha_fin = data.get('fecha_fin')
        marca = data.get('marca')
        valores = get_marcas_USD(fecha_inicio, fecha_fin, marca)
        
        valores_bs = get_marcas_BS(fecha_inicio, fecha_fin, marca)
        
        ventas = []
        unidades = []
        for suma_ventas in valores:
            ventas.append(suma_ventas['total_USD'])
            unidades.append(suma_ventas['cantidad'])
            
        total_usd = sum(ventas)
        total_cantidades = sum(unidades)
        usd = {
            'total_usd': total_usd,
            'total_cantidades': total_cantidades
        }
        
        
        total_bs = []
        
        for i in valores_bs:
            total_bs.append(i['total'])

        suma_total_bs = sum(total_bs)
        
        
        suma_por_tienda = defaultdict(lambda: {"total_USD": 0.0, "cantidad": 0.0})
        
        mapa_tiendas = dict(zip(tiendas_completas, tiendas_simplificadas))
        

        for registro in valores:
            tienda_completa = registro["Tienda"]
            tienda_simplificada = mapa_tiendas.get(tienda_completa, tienda_completa)  
            suma_por_tienda[tienda_simplificada]["total_USD"] += registro.get("total_USD", 0.0)
            suma_por_tienda[tienda_simplificada]["cantidad"] += registro.get("cantidad", 0.0)
        
        

        return jsonify({
            'valores_tienda': suma_por_tienda,
            'total_usd': usd,
            'total_bs': suma_total_bs
        })

    
    

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
