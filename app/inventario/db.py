# Configuración o modelos del módulo
from conexiones.adaptadores import get_db_connection

def inventario_movimiento(deposito, fecha_inicio, base_datos, departamento):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('[dbo].[sp_ObtenerArticulosConUnionesDinamico] @c_CodDeposito = %s , @f_FechaInicio = %s, @BaseDatos = %s, @c_Departamento = %s', 
                   (deposito, fecha_inicio, base_datos, departamento))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    db.close()
    return data


