# Configuración o modelos del módulo
from conexiones.adaptadores_Sqlite import get_db
from conexiones.adaptadores import get_db_connection, get_db_connection_index



def consulta_ventas(fecha_init,fecha_end):
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
    data = pointer.fetchall()
    conexion.close()
    return data




def graficos_por_tiendas(tabla):
        conexion = get_db_connection_index()
        pointer = conexion.cursor()
        pointer.execute(f"""SELECT V_USD as "V_USD" , n_trasacciones FROM {tabla} ORDER BY ID DESC LIMIT 1""")
        columns = [column[0] for column in pointer.description]
        filas = pointer.fetchall()
        data = [dict(zip(columns, fila)) for fila in filas]
        conexion.close()
        for row in data:
            v_usd = row.get('V_USD')
            if isinstance(v_usd, str) and v_usd.lower().startswith('0e'):
                row['V_USD'] = "0.00"
            else:
                # Convertimos a float y redondeamos a 2 decimales, devolvemos como string para mantener formato
                try:
                    row['V_USD'] = f"{float(v_usd):.2f}"
                except (TypeError, ValueError):
                    row['V_USD'] = "0.00"
        return data
    


 
def ventas_al_dia(fecha_init,fecha_end):
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



def tasa_del_dia():
    coneccion =  get_db_connection()
    pointer = coneccion.cursor()
    pointer.execute("select n_factor from MA_MONEDAS where c_codmoneda in ('USD')")
    columns = [column[0] for column in pointer.description]
    filas = pointer.fetchall()
    data = [dict(zip(columns, fila)) for fila in filas]
    coneccion.close()
    return data[0]

