from conexiones.adaptadores import get_db_connection

def ventas_usd(fecha_inicio, fecha_fin, tienda, server):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('sp_ObtenerResumenPagosUSD_MultiDB_Remoto @FechaInicio = %s , @FechaFin = %s,@NumeroSucursal = %s , @ServidorTienda  = %s',(fecha_inicio, fecha_fin, tienda,server))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    connection.close()
    return data


def transacciones(fecha_inicio, fecha_fin, tienda,server):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('TotalVentasenUSDxTiendas_Remoto  @FechaInicio = %s , @FechaFin = %s,@c_Localidad = %s,@ServidorTienda  = %s',(fecha_inicio, fecha_fin, tienda, server))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    connection.close()
    return data


def ventas_bs(fecha_inicio, fecha_fin, tienda, server):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('TotalVentasenBsxTiendas_Remoto @FechaInicio = %s , @FechaFin = %s,@NumeroSucursal = %s, @ServidorTienda = %s',(fecha_inicio, fecha_fin, tienda,server))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    connection.close()
    return data



def ventas_CSH(fecha_inicio, fecha_fin, tienda, server):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('TotalVentasenUSDxTiendaCSH_Remoto @FechaInicio = %s , @FechaFin = %s,@c_Localidad = %s , @ServidorTienda = %s',(fecha_inicio, fecha_fin, tienda,server))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    connection.close()
    return data


def ventas_efectivo(fecha_inicio, fecha_fin, tienda, server):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('TotalVentasenUSDxTiendaEfectivo_Remoto @FechaInicio = %s , @FechaFin = %s,@c_Localidad = %s ,@ServidorTienda = %s',(fecha_inicio, fecha_fin, tienda, server))
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    connection.close()
    return data


def union_de_funciones_ultimo_update(fecha_inicio, fecha_fin, tienda, server):
    ventas_usd_data = ventas_usd(fecha_inicio, fecha_fin, tienda, server)
    transacciones_data = transacciones(fecha_inicio, fecha_fin, tienda, server)
    ventas_bs_data = ventas_bs(fecha_inicio, fecha_fin, tienda, server)
    ventas_csh_data = ventas_CSH(fecha_inicio, fecha_fin, tienda, server)
    ventas_efectivo_data = ventas_efectivo(fecha_inicio, fecha_fin, tienda, server)

    ventas_usd_serializer ={'ventas_usd_data': ventas_usd_data}
    ventas_bs_serializer = {'ventas_bs_data': ventas_bs_data}
    ventas_csh_serializer = {'ventas_csh_data': ventas_csh_data}
    ventas_efectivo_serializer = {'ventas_efectivo_data': ventas_efectivo_data}
    transacciones_serializer = {'transacciones_data': transacciones_data}

    return ventas_usd_serializer , ventas_bs_serializer , ventas_csh_serializer , ventas_efectivo_serializer , transacciones_serializer














