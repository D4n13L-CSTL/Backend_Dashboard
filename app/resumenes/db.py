# Configuración o modelos del módulo
from conexiones.adaptadores_Sqlite import get_db_db2020_2023
from conexiones.adaptadores import get_db_connection_resumenes

def consulta_fecha(tabla, fecha_init, fecha_final):
    db = get_db_connection_resumenes()
    cursor = db.cursor()
    query = f"""
        SELECT 
            SUM(V_USD) AS total_usd,
            SUM(V_BS) AS total_bs,
            SUM(V_EFEC) AS total_efectivo
        FROM {tabla}
        WHERE fecha BETWEEN %s AND %s
    """
    cursor.execute(query, (fecha_init, fecha_final))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    cursor.close()
    return data




def suma_general_2020_2023(fecha_init,fecha_end):
    conexion = get_db_connection_resumenes()
    pointer = conexion.cursor()
    pointer.execute("""
                    SELECT 
    fecha AS fecha,
    V_USD AS total_usd,
    V_BS AS total_bs,
    V_EFEC AS total_efec
FROM (
    SELECT V_USD, V_BS, V_EFEC, FECHA FROM babilon
    UNION ALL
    SELECT V_USD, V_BS, V_EFEC, FECHA FROM baralt
    UNION ALL
    SELECT V_USD, V_BS, V_EFEC, FECHA FROM cabudare
	UNION ALL
    SELECT V_USD, V_BS, V_EFEC, FECHA FROM cagua
	UNION ALL
    SELECT V_USD, V_BS, V_EFEC, FECHA FROM cabimas
	UNION ALL
    SELECT V_USD, V_BS, V_EFEC, FECHA FROM catia
	UNION ALL
    SELECT V_USD, V_BS, V_EFEC, FECHA FROM cruzverde
	UNION ALL
    SELECT V_USD, V_BS, V_EFEC, FECHA FROM guacara
	UNION ALL
    SELECT V_USD, V_BS, V_EFEC, FECHA FROM guanare
	UNION ALL
    SELECT V_USD, V_BS, V_EFEC, FECHA FROM kapitana
	UNION ALL
    SELECT V_USD, V_BS, V_EFEC, FECHA FROM maturin
	UNION ALL
    SELECT V_USD, V_BS, V_EFEC, FECHA FROM propatria
	UNION ALL
    SELECT V_USD, V_BS, V_EFEC, FECHA FROM upata
	UNION ALL
    SELECT V_USD, V_BS, V_EFEC, FECHA FROM valencia
	UNION ALL
    SELECT V_USD, V_BS, V_EFEC, FECHA FROM valera
) AS todas_las_tablas
WHERE FECHA BETWEEN %s AND %s
                    """,(fecha_init,fecha_end))
    columns = [column[0] for column in pointer.description]
    rows = pointer.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    conexion.close()
    return data



def tiendas_sumadas(fechaInit,fechaFin):
    sucursales = [
        'BABILON', 'BARALT', 'CABUDARE', 'CAGUA', 'CABIMAS',
        'CATIA', 'CRUZVERDE', 'GUACARA', 'GUANARE', 'KAPITANA',
        'MATURIN', 'PROPATRIA', 'UPATA', 'VALENCIA', 'VALERA'
    ] 
    diccionario = {}
    for i in sucursales:
        valor = consulta_fecha(i,fechaInit,fechaFin)
        diccionario[i] = valor
    
    return diccionario