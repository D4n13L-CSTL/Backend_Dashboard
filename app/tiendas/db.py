# Configuración o modelos del módulo
from conexiones.adaptadores_Sqlite import get_db
from conexiones.adaptadores import get_db_connection_index

def ventas_tiendas(tienda, fecha_inicio, fecha_fin):
        conexion = get_db_connection_index()
        pointer = conexion.cursor()
        pointer.execute(f"SELECT * FROM {tienda} WHERE FECHA BETWEEN  %s AND  %s",(fecha_inicio, fecha_fin))
        colums = [colum[0] for colum in pointer.description]
        rows = pointer.fetchall()
        data = [dict(zip(colums,row))for  row in rows]
        conexion.close()
        return  data
    
    
    
def ventas_tiendas_diarias(tienda):
        conexion = get_db_connection_index()
        pointer = conexion.cursor()
        pointer.execute(f"SELECT * FROM {tienda} ORDER BY ID DESC LIMIT 1 ")
        colums = [colum[0] for colum in pointer.description]
        rows = pointer.fetchall()
        data = [dict(zip(colums,row))for  row in rows]
        conexion.close()
        return  data