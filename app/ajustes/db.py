from conexiones.adaptadores import get_db_connection

def ajustes(tienda, fecha_inicio, fecha_fin):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("sp_Cabecera_ma_inventario @FechaInicio = %s, @FechaFin = %s, @DBName = %s", (fecha_inicio, fecha_fin, tienda))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    conn.close()
    return data


def detalles_de_ajustes(fecha_inicio, fecha_fin, tienda, documento):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('sp_ConsultaTRInventarioAJU @FechaInicio = %s, @FechaFin = %s, @DBName = %s, @Documento = %s', (fecha_inicio, fecha_fin, tienda, documento))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    conn.close()
    return data