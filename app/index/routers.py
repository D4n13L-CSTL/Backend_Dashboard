from flask import Blueprint, jsonify, request
from .db import consulta_ventas, graficos_por_tiendas, ventas_al_dia, tasa_del_dia
from .meses import meses, ultimo_dia_mes
from datetime import datetime,timedelta
from decimal import Decimal, ROUND_HALF_UP


bp = Blueprint('index', __name__, url_prefix='/index')

def obtener_fecha():
    fecha = datetime.now()
    fecha_diaria = fecha.date()
    return fecha_diaria

@bp.route('api/graficosMensuales',methods=['GET'])
def graficos_mensuales_routes():
    hoy = datetime.today()
    año_actual = hoy.year
    mes_actual = hoy.month
    ventas_mensuales = []
    nombres_meses = []
    try:
        for mes, (inicio, fin) in meses.items():

            mes_numero = int(fin.split("-")[1])
           
            if año_actual > 2025 or (año_actual == 2025 and mes_numero < mes_actual):

                resultado = consulta_ventas(inicio, fin)
                if resultado and len(resultado) > 0:
                    ventas_mensuales.append(resultado[0][0])
                    nombres_meses.append(mes)
                else:
                    print(f"No hay datos para {mes}")

        grafico_mensuales = ventas_mensuales
    
        nombres_meses = nombres_meses
        return jsonify({
            'ventas_mensuales': grafico_mensuales,
            'nombres_meses': nombres_meses
        })    
    
    except Exception as e:
        print(f"Error al procesar los datos: {str(e)}"), 500
    




@bp.route('api/graficosPorTiendas', methods=['GET'])
def graficos_por_tiendas_routes():
    try:
        tablas = [
            'BABILON', 'BARALT', 'CABUDARE', 'CAGUA', 'CABIMAS',
            'CATIA', 'CRUZVERDE', 'GUACARA', 'GUANARE', 'KAPITANA',
            'MATURIN', 'PROPATRIA', 'UPATA', 'VALENCIA', 'VALERA'
        ]
        datos = []
        
        for tabla in tablas:
            data = graficos_por_tiendas(tabla)
            if data:
                datos.append({tabla: data})

        return jsonify(datos)

    except Exception as e:
        print(f"Error al procesar los datos: {str(e)}")
        return jsonify({"error": "Error al procesar los datos"}), 500

    
    
  
  
@bp.route('api/ventasPorFecha', methods=['GET'])
def ventas_por_fecha():
    try:

        raw_data = ventas_al_dia(str(obtener_fecha()), str(obtener_fecha()))
        data = {}
        for key, value in raw_data.items():
            decimal_value = Decimal(value)

            if decimal_value.is_zero():
                decimal_value = Decimal('0.00')

            # Redondear a 2 decimales
            rounded = decimal_value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

            data[key] = float(rounded)  # o str(rounded)

        return jsonify(data)
        

    except Exception as e:
        print(f"Error al procesar los datos: {str(e)}")
        return jsonify({"error": "Error al procesar los datos"}), 500
    
    
    
  
@bp.route('api/tasa', methods=['GET'])
def tasa_route():
    try:

        data =tasa_del_dia()
        return jsonify(data)

    except Exception as e:
        print(f"Error al procesar los datos: {str(e)}")
        return jsonify({"error": "Error al procesar los datos"}), 500
    
    
    