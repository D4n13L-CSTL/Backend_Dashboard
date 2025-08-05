# Configuración o modelos del módulo
from conexiones.adaptadores_Sqlite import get_db, get_db_db2020_2023, get_db_db2024



def valores_meses(tienda):
    conexion = get_db_db2020_2023()
    cursor = conexion.cursor()
    cursor.execute(f"""
                   SELECT *
                    FROM {tienda} 
                    where FECHA BETWEEN '2020-01-01' and '2023-12-31'
                    ORDER by FECHA ASC
                   """)
    columns = [i[0] for i in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    conexion.close()
    return data


def valores_meses_general():
    conexion = get_db_db2020_2023()
    cursor = conexion.cursor()
    cursor.execute(f"""
                    SELECT 
                    V_USD,
                    V_BS,
                    FECHA
                FROM (
                    SELECT V_USD, V_BS, FECHA FROM babilon
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM baralt
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM cabudare
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM cagua
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM cabimas
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM catia
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM cruzverde
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM guacara
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM guanare
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM kapitana
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM maturin
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM propatria
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM upata
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM valencia
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM valera
                ) AS todas_las_tablas
                WHERE FECHA BETWEEN '2020-01-01' AND '2023-12-31'
                ORDER BY FECHA ASC
                   """)
    columns = [i[0] for i in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    conexion.close()
    return data


def valores_meses_general_2024():
    conexion = get_db_db2024()
    cursor = conexion.cursor()
    cursor.execute(f"""
                    SELECT 
                        (V_USD),
                        (V_BS) ,
                        (FECHA)
                    FROM (
                        SELECT V_USD, V_BS, FECHA FROM BABILON
                        UNION ALL
                        SELECT V_USD, V_BS, FECHA FROM BARALT
                        UNION ALL
                        SELECT V_USD, V_BS, FECHA FROM CABUDARE
                        UNION ALL
                        SELECT V_USD, V_BS, FECHA FROM CAGUA
                        UNION ALL
                        SELECT V_USD, V_BS, FECHA FROM CABIMAS
                        UNION ALL
                        SELECT V_USD, V_BS, FECHA FROM CATIA
                        UNION ALL
                        SELECT V_USD, V_BS, FECHA FROM CRUZ_VERDE
                        UNION ALL
                        SELECT V_USD, V_BS, FECHA FROM GUACARA
                        UNION ALL
                        SELECT V_USD, V_BS, FECHA FROM GUANARE
                        UNION ALL
                        SELECT V_USD, V_BS, FECHA FROM KAPITANA
                        UNION ALL
                        SELECT V_USD, V_BS, FECHA FROM MATURIN
                        UNION ALL
                        SELECT V_USD, V_BS, FECHA FROM PROPATRIA
                        UNION ALL
                        SELECT V_USD, V_BS, FECHA FROM UPATA
                        UNION ALL
                        SELECT V_USD, V_BS, FECHA FROM VALENCIA
                        UNION ALL
                        SELECT V_USD, V_BS, FECHA FROM VALERA
                    ) AS todas_las_tablas
                    WHERE FECHA BETWEEN '2024-01-01' AND '2024-12-31'
                   """)
    columns = [i[0] for i in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    conexion.close()
    return data


def valores_meses_general_2025():
    conexion = get_db()
    cursor = conexion.cursor()
    cursor.execute(f"""
                    SELECT 
                    sum(V_USD) AS V_USD,
					sum(V_BS)AS V_BS,
					FECHA
                FROM (
                    SELECT V_USD, V_BS, FECHA FROM babilon
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM baralt
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM cabudare
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM cagua
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM cabimas
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM catia
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM CRUZ_VERDE
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM guacara
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM guanare
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM kapitana
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM maturin
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM propatria
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM upata
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM valencia
                    UNION ALL
                    SELECT V_USD, V_BS, FECHA FROM valera
                ) AS todas_las_tablas
                WHERE FECHA BETWEEN '2025-01-01' AND '2025-12-31'
                ORDER BY FECHA ASC
                   """)
    columns = [i[0] for i in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    conexion.close()
    return data


def valores_meses_2025(tienda):
    conexion = get_db()
    cursor = conexion.cursor()
    if tienda == "Cruzverde":
        tienda = "CRUZ_VERDE"
    cursor.execute(f"""
                   SELECT *
                    FROM {tienda} 
                    where FECHA BETWEEN '2025-01-01' and '2025-12-31'
                    ORDER by FECHA ASC
                   """)
    columns = [i[0] for i in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    conexion.close()
    return data





def valores_meses_2024(tienda):
    conexion = get_db_db2024()
    if tienda == "Cruzverde":
        tienda = "CRUZ_VERDE"
    cursor = conexion.cursor()
    cursor.execute(f"""
                   SELECT *
                    FROM {tienda} 
                    where FECHA BETWEEN '2024-01-01' and '2024-12-31'
                    ORDER by FECHA ASC
                   """)
    columns = [i[0] for i in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    conexion.close()
    return data



def llamada(tienda):
    valores1 = valores_meses(tienda)
    valores2 = valores_meses_2024(tienda)
    valores3 = valores_meses_2025(tienda)

    data = valores1 + valores2 + valores3
    return data

def llamada_general():
    valores1 = valores_meses_general()
    valores2 = valores_meses_general_2024()
    valores3 = valores_meses_general_2025()

    data = valores1 + valores2 + valores3
    return data