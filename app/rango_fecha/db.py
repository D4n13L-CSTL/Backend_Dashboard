# Configuración o modelos del módulog
from conexiones.adaptadores_Sqlite import get_db
from conexiones.adaptadores import get_db_connection_index

def consulta_fecha(fecha_init,fecha_end):
    conexion = get_db_connection_index()
    pointer = conexion.cursor()
    pointer.execute("""
                    SELECT 
    SUM(V_USD) AS total_usd,
    SUM(V_BS) AS total_bs,
    SUM(V_CSH) AS total_csh,
    SUM(V_EFEC) AS total_efec
FROM (
    SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA FROM BABILON
    UNION ALL
    SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA FROM BARALT
    UNION ALL
    SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA FROM CABUDARE
	UNION ALL
    SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA FROM CAGUA
	UNION ALL
    SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA FROM CABIMAS
	UNION ALL
    SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA FROM CATIA
	UNION ALL
    SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA FROM CRUZVERDE
	UNION ALL
    SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA FROM GUACARA
	UNION ALL
    SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA FROM GUANARE
	UNION ALL
    SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA FROM KAPITANA
	UNION ALL
    SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA FROM MATURIN
	UNION ALL
    SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA FROM PROPATRIA
	UNION ALL
    SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA FROM UPATA
	UNION ALL
    SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA FROM VALENCIA
	UNION ALL
    SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA FROM VALERA
) AS todas_las_tablas
WHERE FECHA BETWEEN %s AND %s;
""",(fecha_init,fecha_end))
    columns = [column[0] for column in pointer.description]
    filas = pointer.fetchall()
    data = [dict(zip(columns, fila)) for fila in filas]
    conexion.close()
    return data[0]





def consulta_fecha_por_sucursal(fecha_init, fecha_end, sucursal):
    conexion = get_db_connection_index()
    pointer = conexion.cursor()
    pointer.execute(f"""
                    SELECT 
            SUM(V_USD) AS total_usd,
            SUM(n_trasacciones) AS unidades_vendidas
        FROM (
            SELECT V_USD, V_BS, V_CSH, V_EFEC, FECHA,n_trasacciones FROM {sucursal}
        ) AS todas_las_tablas
        WHERE FECHA BETWEEN %s AND %s;
""",(fecha_init,fecha_end))
    columns = [column[0] for column in pointer.description]
    filas = pointer.fetchall()
    data = [dict(zip(columns, fila)) for fila in filas]
    conexion.close()
    return data[0]


def llamada_de_funciones(fecha_init,fecha_end):
    valores = consulta_fecha(fecha_init, fecha_end)
    sucursales = [
        'BABILON', 'BARALT', 'CABUDARE', 'CAGUA', 'CABIMAS',
        'CATIA', 'CRUZVERDE', 'GUACARA', 'GUANARE', 'KAPITANA',
        'MATURIN', 'PROPATRIA', 'UPATA', 'VALENCIA', 'VALERA'
    ] 
    valores_por_sucursal = {}
    for sucursal in sucursales:
        valores_por_sucursal[sucursal] = consulta_fecha_por_sucursal(fecha_init, fecha_end, sucursal)

    return valores , valores_por_sucursal


