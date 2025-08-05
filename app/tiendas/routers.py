from flask import Blueprint, jsonify , request
from .db import ventas_tiendas, ventas_tiendas_diarias
from .meses import mes_init, mes_fin
from .semanas import semanas_variadas,año,meses
from datetime import datetime, timedelta, date
bp = Blueprint('tiendas', __name__, url_prefix='/tiendas')

fecha = datetime.now()
def obter_fecha():
    fecha_ddef = datetime.now()
    fecha_diaria = fecha_ddef.date()
    return fecha_diaria
mes_date = obter_fecha().month
mes_actual = f'{mes_date:02d}'

def obtener_fecha_sistema():
    fecha_sistema = datetime.now().date() 
    return fecha_sistema

@bp.route('/<tienda>', methods=['GET'])
def index(tienda):

        grafico = ventas_tiendas(tienda, mes_init[0], mes_fin[11])
        
        fecha_sistema = obtener_fecha_sistema()
        
        inicio_semana = fecha_sistema - timedelta(days=fecha_sistema.weekday())  
        
        fechas_semana = [(inicio_semana + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]
        
        ventas_semanales = [None] * 7 #GRAFICO DE DIAS
        
        for registro in grafico:
            fecha_valor = registro['fecha']
            if isinstance(fecha_valor, str):
                fecha_obj = datetime.strptime(fecha_valor, '%a, %d %b %Y %H:%M:%S %Z').date()
            elif isinstance(fecha_valor, datetime):
                fecha_obj = fecha_valor.date()
            elif isinstance(fecha_valor, date):
                fecha_obj = fecha_valor
            else:
                continue  

            fecha_str = fecha_obj.strftime('%Y-%m-%d')  

            if fecha_str in fechas_semana:
                indice_dia = fechas_semana.index(fecha_str)
                ventas_semanales[indice_dia] = registro['v_usd'] 

        
        
        semanas = {semana: [] for semana in range(1, 7)}
        
        rango_semanas = [
            (
                datetime.strptime(f'{año}-{mes_actual}-{min([d for d in semana if d > 0]):02d}', '%Y-%m-%d').date(),
                datetime.strptime(f'{año}-{mes_actual}-{max([d for d in semana if d > 0]):02d}', '%Y-%m-%d').date()
            )
            for semana in semanas_variadas if any(d > 0 for d in semana)
        ]
        
        
        # Iterar sobre los datos en grafico_mensuales
        for j in grafico:
            fecha_valor = j['fecha']
            if isinstance(fecha_valor, str):
                fecha_actual = datetime.strptime(fecha_valor, '%a, %d %b %Y %H:%M:%S %Z').date()
            elif isinstance(fecha_valor, datetime):
                fecha_actual = fecha_valor.date()
            elif isinstance(fecha_valor, date):
                fecha_actual = fecha_valor
            else:
                raise TypeError(f"Tipo de fecha inesperado: {type(fecha_valor)}")

            for i, (inicio, fin) in enumerate(rango_semanas, 1):
                if inicio <= fecha_actual <= fin:
                    semanas[i].append((j['v_usd'], j['v_csh'], j['v_bs'], j['v_efec']))
                    break


        usds_semanal = {semana: [response[0] for response in semanas[semana]] for semana in range(1, 7)}
        csh_semanal = {semana: [response[1] for response in semanas[semana]] for semana in range(1, 7)}
        bs_semanal = {semana: [response[2] for response in semanas[semana]] for semana in range(1, 7)}
        efe_semanal = {semana: [response[3] for response in semanas[semana]] for semana in range(1, 7)}
        
        #LISTA GRAFICO SEMANAL
        weekly_sales = [sum(usds_semanal[1]), sum(usds_semanal[2]), sum(usds_semanal[3]),sum(usds_semanal[4]),sum(usds_semanal[5]), sum(usds_semanal[6])]
        suma_semanal_csh =[sum(csh_semanal[1]), sum(csh_semanal[2]),sum(csh_semanal[3]),sum(csh_semanal[4]),sum(csh_semanal[5]), sum(csh_semanal[6])]
        suma_semanal_bs = [sum(bs_semanal[1]), sum(bs_semanal[2]),sum(bs_semanal[3]),sum(bs_semanal[4]),sum(bs_semanal[5]),sum(bs_semanal[6])] 
        suma_semanal_efectivo = [sum(efe_semanal[1]), sum(efe_semanal[2]),sum(efe_semanal[3]),sum(efe_semanal[4]),sum(efe_semanal[5]), sum(efe_semanal[6])]
        
        
        
        meses = {month: [] for month in range(1, 13)}  # Diccionario de meses (1 a 12)
        
        
        for valores in grafico:
            fecha_valor = valores['fecha']
            if isinstance(fecha_valor, str):
                fecha_actual = datetime.strptime(fecha_valor, '%a, %d %b %Y %H:%M:%S %Z').date()
            elif isinstance(fecha_valor, datetime):
                fecha_actual = fecha_valor.date()
            elif isinstance(fecha_valor, date):
                fecha_actual = fecha_valor
            else:
                raise TypeError(f"Tipo de fecha inesperado: {type(fecha_valor)}")


            mes = fecha_actual.month
            meses[mes].append((valores['v_usd'], valores['v_csh'], valores['v_bs'], valores['v_efec']))
            
            
        usds = {month: [tupla[0] for tupla in meses[month]] for month in range(1, 13)}
        csh = {month: [tupla[1] for tupla in meses[month]] for month in range(1, 13)}
        bs = {month: [tupla[2] for tupla in meses[month]] for month in range(1, 13)}
        efe = {month: [tupla[3] for tupla in meses[month]] for month in range(1, 13)}
        
        usd_mensual = [sum(usds[1])+ sum(usds[2]) + sum(usds[3])+ sum(usds[4])+ sum(usds[5])+ sum(usds[6])+ sum(usds[7])+ sum(usds[8])+ sum(usds[8])+ sum(usds[10])+ sum(usds[11])+ sum(usds[12])]
        bs_mensual = [sum(bs[1]) + sum(bs[2]) + sum(bs[3])+ sum(bs[4])+ sum(bs[5])+ sum(bs[6])+ sum(bs[7])+ sum(bs[8])+ sum(bs[9])+ sum(bs[10])+ sum(bs[11])+ sum(bs[12]) ]
        csh_mensual = [sum(csh[1]) + sum(csh[2])+ sum(csh[3])+ sum(csh[4])+ sum(csh[5])+ sum(csh[6])+ sum(csh[7])+ sum(csh[8])+ sum(csh[9])+ sum(csh[10])+ sum(csh[11])+ sum(csh[12])]
        efect_mensual = [sum(efe[1]) + sum(efe[2])+ sum(efe[3])+ sum(efe[4])+ sum(efe[5])+ sum(efe[6])+ sum(efe[7])+ sum(efe[8])+ sum(efe[9])+ sum(efe[10])+ sum(efe[11])+ sum(efe[12])]
        
        #LISTA DEL GRAFICO MENSUAL
        monthly_sales = []
        
        fecha_hoy = obter_fecha()  # asumo que retorna un date o datetime
        if isinstance(fecha_hoy, str):
            fecha_hoy = datetime.strptime(fecha_hoy, "%Y-%m-%d").date()

        monthly_sales = [
            sum(usds[mes]) if date.today().month >= mes else 0
            for mes in range(1, 13)
        ]


        ventas_diarias = ventas_tiendas_diarias(tienda)

        valores_diarios = {
            "ventas_usd": float(ventas_diarias[0]['v_usd']),
            "ventas_csh": float(ventas_diarias[0]['v_csh']),
            "ventas_bs": float(ventas_diarias[0]['v_bs']),
            "ventas_efectivo": float(ventas_diarias[0]['v_efec'])
        }

        valores_semanales = {
            "ventas_usd": float(sum(weekly_sales)),
            "ventas_csh": float(sum(suma_semanal_csh)),
            "ventas_bs": float(sum(suma_semanal_bs)),
            "ventas_efectivo": float(sum(suma_semanal_efectivo))
        }

        valores_mensuales = {
            "ventas_usd": float(sum(usd_mensual)),
            "ventas_csh": float(sum(csh_mensual)),
            "ventas_bs": float(sum(bs_mensual)),
            "ventas_efectivo": float(sum(efect_mensual))
        }

        return jsonify({
            "grafico_diario": ventas_semanales,
            "grafico_semanal": weekly_sales,
            "grafico_mensual": monthly_sales,
            "ventas_diarias": valores_diarios,
            "ventas_semanal": valores_semanales,
            "ventas_mensual": valores_mensuales
        })