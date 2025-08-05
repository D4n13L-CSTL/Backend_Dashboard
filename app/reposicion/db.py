# Configuración o modelos del módulo
from conexiones.adaptadores import get_db_connection

def reposicion(codigo, fecha_inicio,fecha_fin):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute('[dbo].[sp_AnalisisInventario] @FechaInicio = %s, @FechaFin = %s, @CodArticulo = %s', (fecha_inicio, fecha_fin, codigo))
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        data = [dict(zip(columns, row)) for row in rows]
        db.close()
        return data
    