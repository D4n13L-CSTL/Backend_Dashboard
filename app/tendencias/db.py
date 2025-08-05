# Configuración o modelos del módulo
from conexiones. adaptadores import  get_db_connection_index
from collections import defaultdict
from .tiendas import tiendas_completas, tiendas_simplificadas




def ventas_por_tendencias(fecha_inicio, fecha_fin): 
    connection = get_db_connection_index()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM public.tendencias where fecha between %s and %s", (fecha_inicio, fecha_fin)) #SP PARA TENDENCIAS
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    connection.close()
    return data



def retorno_serializado(fecha_inicio, fecha_fin, dpto):
    valores = ventas_por_tendencias(fecha_inicio, fecha_fin)
    suma_por_tienda = defaultdict(lambda: {"total_USD": 0.0, "cantidad": 0.0, "producto_mas_vendido": {"nombre": None, "cantidad": 0, "codigo": None}})
    mapa_tiendas = dict(zip(tiendas_completas, tiendas_simplificadas))
    total_usd = 0.0
    total_cantidad = 0.0
    
    productos_por_tienda = defaultdict(lambda: defaultdict(lambda: {"cantidad": 0.0, "codigo": "N/A"}))
    
    for registro in valores:
            if registro.get("c_Departamento") == dpto:
                tienda_completa = registro["BaseDatos"]
                tienda_simplificada = mapa_tiendas.get(tienda_completa, tienda_completa)
                
                valor_flotante = float(registro.get("total", 0.0)) if registro.get("total") else 0.0
                cantidad_flotante = float(registro.get("cantidad", 0.0)) if registro.get("cantidad") else 0.0
                
                producto = registro.get("c_Descri", "Desconocido")
                codigo_articulo = registro.get("cod_principal", "N/A")
                
                suma_por_tienda[tienda_simplificada]["total_USD"] += valor_flotante
                suma_por_tienda[tienda_simplificada]["cantidad"] += cantidad_flotante
                productos_por_tienda[tienda_simplificada][producto]["cantidad"] += cantidad_flotante
                productos_por_tienda[tienda_simplificada][producto]['codigo'] = codigo_articulo
                
                total_usd += valor_flotante
                total_cantidad += cantidad_flotante
                
    for tienda, productos in productos_por_tienda.items():
            if productos:
                producto_mas_vendido = max(productos, key=lambda p: productos[p]["cantidad"])
                suma_por_tienda[tienda]["producto_mas_vendido"] = {
                    "nombre": producto_mas_vendido,
                    "codigo": productos[producto_mas_vendido]["codigo"],
                    "cantidad": productos[producto_mas_vendido]["cantidad"]}
    
    resultado = {
            "filtro": dpto,
            "valores_tiendas": dict(suma_por_tienda),
            "total_usd": total_usd,
            "total_cantidad": total_cantidad
        }      
    
    return resultado




def cantidades(fechaini, fechafin):
    connection = get_db_connection_index()
    cursor = connection.cursor()
    cursor.execute("""select "c_Departamento" as Deptos, sum(cantidad) from tendencias  where fecha between %s  and %s
        group by Deptos""",(fechaini, fechafin))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    connection.close()
    return data