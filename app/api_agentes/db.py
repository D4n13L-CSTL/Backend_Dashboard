from conexiones.adaptadores import get_db_connection

def ventas_usd(fecha_inicio, fecha_fin, tienda):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('sp_ObtenerResumenPagosUSD_MultiDB @FechaInicio = %s , @FechaFin = %s,@NumeroSucursal = %s',(fecha_inicio, fecha_fin, tienda))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    connection.close()
    return data


def transacciones(fecha_inicio, fecha_fin, tienda):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('TotalVentasenUSDxTiendas @FechaInicio = %s , @FechaFin = %s,@c_Localidad = %s',(fecha_inicio, fecha_fin, tienda))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    connection.close()
    return data


def ventas_bs(fecha_inicio, fecha_fin, tienda):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('TotalVentasenBsxTiendas @FechaInicio = %s , @FechaFin = %s,@c_Localidad = %s',(fecha_inicio, fecha_fin, tienda))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    connection.close()
    return data


def ventas_CSH(fecha_inicio, fecha_fin, tienda):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('TotalVentasenUSDxTiendaCSH @FechaInicio = %s , @FechaFin = %s,@c_Localidad = %s',(fecha_inicio, fecha_fin, tienda))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    connection.close()
    return data


def ventas_efectivo(fecha_inicio, fecha_fin, tienda):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('TotalVentasenUSDxTiendaEfectivo @FechaInicio = %s , @FechaFin = %s,@c_Localidad = %s',(fecha_inicio, fecha_fin, tienda))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    connection.close()
    return data


def union_de_funciones(fecha_inicio, fecha_fin, tienda):
    ventas_usd_data = ventas_usd(fecha_inicio, fecha_fin, tienda)
    transacciones_data = transacciones(fecha_inicio, fecha_fin, tienda)
    ventas_bs_data = ventas_bs(fecha_inicio, fecha_fin, tienda)
    ventas_csh_data = ventas_CSH(fecha_inicio, fecha_fin, tienda)
    ventas_efectivo_data = ventas_efectivo(fecha_inicio, fecha_fin, tienda)

    ventas_usd_serializer ={'ventas_usd_data': ventas_usd_data}
    ventas_bs_serializer = {'ventas_bs_data': ventas_bs_data}
    ventas_csh_serializer = {'ventas_csh_data': ventas_csh_data}
    ventas_efectivo_serializer = {'ventas_efectivo_data': ventas_efectivo_data}
    transacciones_serializer = {'transacciones_data': transacciones_data}

    return ventas_usd_serializer , ventas_bs_serializer , ventas_csh_serializer , ventas_efectivo_serializer , transacciones_serializer








def ventas_por_departamento(fecha_inicio, fecha_fin): #CONSULTA PARA AGENTE DE DEPARTAMENTOS
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SP_ReporteDetalladoVentasTiendasUSDOptimizado @FechaInicio = %s, @FechaFin = %s', (fecha_inicio, fecha_fin))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    connection.close()
    return data







def ventas_por_tendencias(fecha_inicio, fecha_fin): #CONSULTA PARA AGENTE DE TENDENCIAS
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('sp_ConsultaInventarioMultiDB7 @FechaInicio = %s, @FechaFin = %s', (fecha_inicio, fecha_fin)) #SP PARA TENDENCIAS
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    connection.close()
    return data






