# Configuración o modelos del módulo
from conexiones.adaptadores import get_db_connection

def get_marcas_USD(fecha_inicio, fecha_fin, marca):
    conexion = get_db_connection()
    cursor = conexion.cursor()
    parametro_marca = f'%{marca}%'
    cursor.execute("sp_reportes_ventas_productos @FechaInicio = %s, @FechaFin = %s , @Filtro  = %s ",(fecha_inicio, fecha_fin, parametro_marca))              
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    conexion.close()
    return data


def get_marcas_BS(fecha_inicio, fecha_fin, marca):
    conexion = get_db_connection()
    cursor = conexion.cursor()
    parametro_marca = f'%{marca}%'
    cursor.execute("sp_reportes_ventas_productos_VES @FechaInicio = %s, @FechaFin = %s , @Filtro  = %s ",(fecha_inicio, fecha_fin, parametro_marca))              
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    conexion.close()
    return data




