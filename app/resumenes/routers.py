from flask import Blueprint, request, jsonify
from .db import consulta_fecha,suma_general_2020_2023, tiendas_sumadas
from collections import defaultdict
from datetime import datetime,date

bp = Blueprint('resumenes', __name__, url_prefix='/resumenes')

@bp.route('api/resumenes/<year>', methods=['GET'])
def total_resumenes_route(year):
    try:    
        if year == '2023':
            general = suma_general_2020_2023('2023-01-01', '2023-12-31')

            tiendas_var = tiendas_sumadas('2023-01-01', '2023-12-31')
        elif year == '2022':
           general = suma_general_2020_2023('2022-01-01', '2022-12-31')
           tiendas_var = tiendas_sumadas('2022-01-01', '2022-12-31')
        elif year == '2021':
            general = suma_general_2020_2023('2021-01-01', '2021-12-31')
            tiendas_var = tiendas_sumadas('2021-01-01', '2021-12-31')
        elif year == '2020':
            general = suma_general_2020_2023('2020-01-01', '2020-12-31')
            tiendas_var = tiendas_sumadas('2020-01-01', '2020-12-31')
        
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

            # Diccionario para acumular las ventas por mes
        ventas_por_mes = defaultdict(lambda: {"total_bs": 0, "total_efec": 0, "total_usd": 0})

        for item in general:
                fecha_str = item["fecha"]  
                if isinstance(fecha_str, (datetime, date)):
                    fecha = fecha_str
                else:
                    fecha = datetime.strptime(fecha_str, '%a, %d %b %Y %H:%M:%S %Z')
                mes = fecha.month
                ventas_por_mes[mes]["total_bs"] += item["total_bs"]
                ventas_por_mes[mes]["total_efec"] += item["total_efec"]
                ventas_por_mes[mes]["total_usd"] += item["total_usd"]

        lista_total = []
        bs = []
        usd = []
        efe =  []
        for mes_num, totales in sorted(ventas_por_mes.items()):
                bs.append(totales["total_bs"])
                usd.append(totales["total_usd"])
                efe.append(totales["total_efec"])
                lista_total.append({"mes":meses[mes_num - 1], "totales": totales})
                
        lista_total.append({ "Total_anuales": {"total_anual_bs":sum(bs),"total_anual_efec":sum(efe), "total_anual_usd":sum(usd)}})
        return  jsonify({"Totales_meses":lista_total, "Tiendas":tiendas_var}), 200
    except Exception as e:
            return jsonify({"error": str(e)}), 500
        
        






@bp.route('api/resumenes/<year>/<tienda>', methods=['GET', 'POST'])
def resumen2023(year,tienda):
    try:
        if year == '2023':
            valor = consulta_fecha(tienda, '2023-01-01', '2023-12-31')
        elif year == '2022':
            valor = consulta_fecha(tienda, '2022-01-01', '2022-12-31')
        elif year == '2021':
            valor = consulta_fecha(tienda, '2021-01-01', '2021-12-31')
        elif year == '2020':
            valor = consulta_fecha(tienda, '2020-01-01', '2020-12-31')
        
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

        ventas_por_mes = defaultdict(lambda: {"total_bs": 0, "total_efec": 0, "total_usd": 0})

        for item in valor:
            fecha = datetime.strptime(item["FECHA"], "%Y-%m-%d")
            mes = fecha.month  # 1 a 12
            ventas_por_mes[mes]["total_bs"] += item["V_BS"]
            ventas_por_mes[mes]["total_efec"] += item["EFECTIVO"]
            ventas_por_mes[mes]["total_usd"] += item["V_USD"]


        lista_total = []
        bs = []
        usd = []
        efe =  []
        for mes_num, totales in sorted(ventas_por_mes.items()):
            bs.append(totales["total_bs"])
            usd.append(totales["total_usd"])
            efe.append(totales["total_efec"])
            lista_total.append({"mes":meses[mes_num - 1], "totales": totales})


        lista_total.append({ "Total_anuales": {"total_anual_bs":sum(bs),"total_anual_efec":sum(efe), "total_anual_usd":sum(usd)}})
        return jsonify(lista_total), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500