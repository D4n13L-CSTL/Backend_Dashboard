# Configuración o modelos del módulo
from conexiones.adaptadores import get_db_connection, get_db_connection_deptos
from conexiones.adaptadores_Sqlite import get_db_departamentos

def get_deptos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MA_DEPARTAMENTOS")
    cols = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data  = [dict(zip(cols, row)) for row in rows]
    cursor.close()
    conn.close()
    return data

def grupos_for_departamento(departamento):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MA_GRUPOS WHERE C_DEPARTAMENTO = %s", (departamento,))
    cols = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data  = [dict(zip(cols, row)) for row in rows]
    cursor.close()
    conn.close()
    return data



def grupos_subgrupo_for_departamento(departamento,grupo): #SUBGRUPOS
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MA_SUBGRUPOS WHERE c_in_grupo = %s AND c_in_departamento = %s", (grupo, departamento))
    cols = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data  = [dict(zip(cols, row)) for row in rows]
    cursor.close()
    conn.close()
    return data




#/////////////////////////////////////////////////////////////////////////////////

def consulta_departamentos_filtro_tiendas(fechaInicio,FechaFin, departamento):
    conecion  = get_db_connection_deptos()
    cursor = conecion.cursor()
    cursor.execute("""
               SELECT Tienda, SUM(total) AS suma_total, SUM(cantidad) AS suma_cantidad
                    FROM (
                        SELECT Tienda, total, cantidad, FechaTransaccion, Departamento FROM ENERO
                        UNION ALL
                        SELECT Tienda, total, cantidad, FechaTransaccion, Departamento FROM FEBRERO
                        UNION ALL
                        SELECT Tienda, total, cantidad, FechaTransaccion, Departamento FROM MARZO
                        UNION ALL
                        SELECT Tienda, total, cantidad, FechaTransaccion, Departamento FROM ABRIL
                        UNION ALL
                        SELECT Tienda, total, cantidad, FechaTransaccion, Departamento FROM MAYO
                        UNION ALL
                        SELECT Tienda, total, cantidad, FechaTransaccion, Departamento FROM JUNIO
                        UNION ALL
                        SELECT Tienda, total, cantidad, FechaTransaccion, Departamento FROM JULIO
                        UNION ALL
                        SELECT Tienda, total, cantidad, FechaTransaccion, Departamento FROM AGOSTO
                        UNION ALL
                        SELECT Tienda, total, cantidad, FechaTransaccion, Departamento FROM SEPTIEMBRE
                        UNION ALL
                        SELECT Tienda, total, cantidad, FechaTransaccion, Departamento FROM OCTUBRE
                        UNION ALL
                        SELECT Tienda, total, cantidad, FechaTransaccion, Departamento FROM NOVIEMBRE
                        UNION ALL
                        SELECT Tienda, total, cantidad, FechaTransaccion, Departamento FROM DICIEMBRE
                    ) AS todos
                WHERE FechaTransaccion BETWEEN %s AND %s  
                AND Departamento = %s
                GROUP BY Tienda
                ORDER BY suma_total DESC;        
                   """,(fechaInicio,FechaFin, departamento))
    columns = [i[0] for i in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows] 
    conecion.close()
    return data




#/////////////////////////////////////////////////////////////////////////




def consulta_departamentos_grupo_filtro_tiendas(fechaInicio,FechaFin, departamento, grupo):
    conecion  = get_db_connection_deptos()
    cursor = conecion.cursor()
    cursor.execute("""
            SELECT Tienda, SUM(total) AS suma_total, SUM(cantidad) AS suma_cantidad
            FROM (
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM ENERO
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM FEBRERO
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM MARZO
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM ABRIL
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM MAYO
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM JUNIO
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM JULIO
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM AGOSTO
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM SEPTIEMBRE
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM OCTUBRE
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM NOVIEMBRE
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM DICIEMBRE
            ) AS todos
            WHERE FechaTransaccion BETWEEN %s AND %s
            AND Departamento = %s
            AND substr(cod_principal, 3, 2) = %s
            GROUP BY Tienda
            ORDER BY suma_total DESC;
      
                   """,(fechaInicio,FechaFin, departamento, grupo))
    columns = [i[0] for i in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows] 
    conecion.close()
    return data



#//////////////////////////////////////////////////////////////////////////////////////////////////////





def consulta_departamentos_grupo_subgrupo_filtro_tiendas(fechaInicio,FechaFin, departamento, grupo, subgrupo):
    conecion  = get_db_connection_deptos()
    cursor = conecion.cursor()
    cursor.execute("""
                    SELECT Tienda,
                        SUM(total) AS suma_total,
                        SUM(cantidad) AS suma_cantidad
                    FROM (
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM ENERO
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM FEBRERO
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM MARZO
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM ABRIL
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM MAYO
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM JUNIO
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM JULIO
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM AGOSTO
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM SEPTIEMBRE
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM OCTUBRE
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM NOVIEMBRE
                        UNION ALL
                        SELECT Tienda ,total, cantidad, FechaTransaccion, Departamento, cod_principal FROM DICIEMBRE
                    ) AS todos
                WHERE FechaTransaccion BETWEEN %s AND %s  
                AND Departamento = %s
                AND substr(cod_principal, 3, 2) = %s
                AND substr(cod_principal, 5, 3) = %s
                GROUP BY Tienda
                ORDER BY suma_total DESC;
                   """,(fechaInicio,FechaFin, departamento, grupo, subgrupo))
    columns = [i[0] for i in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows] 
    conecion.close()
    return data

