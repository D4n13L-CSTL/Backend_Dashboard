from flask import Blueprint, jsonify, request
from .db import get_deptos,  consulta_departamentos_grupo_filtro_tiendas ,consulta_departamentos_filtro_tiendas,grupos_for_departamento, grupos_subgrupo_for_departamento,consulta_departamentos_grupo_subgrupo_filtro_tiendas
from .dic import valores_

bp = Blueprint('deptos', __name__, url_prefix='/deptos')

@bp.route('api/deptos', methods=['GET'])
def depto_route():
    valor = get_deptos()
    depato = []
    for i in valor:
        resultado = {"codigo":None, "Descripcion": None}
        resultado["codigo"] = i.get("C_CODIGO")
        resultado["Descripcion"] = i.get("C_DESCRIPCIO")
        depato.append(resultado)
    
    return jsonify(depato)


@bp.route('api/grupos', methods=['POST'])
def grupos_route():
    data = request.json
    departamento = data['codigo_departamento']
    codigo_ = valores_.get(departamento)
    valor = grupos_for_departamento(codigo_)
    grupo = []
    for i in valor:
        resultado = {"codigo":None, "Descripcion": None}
        resultado["codigo"] = i.get("c_CODIGO")
        resultado["Descripcion"] = i.get("C_DESCRIPCIO")
        grupo.append(resultado)
    
    return jsonify(grupo)


@bp.route('api/subgrupo', methods=['POST'])
def subgrupo_route():
    data = request.json
    departamento = data['codigo_departamento']
    codigo_departamento = valores_.get(departamento)
    grupo = data['codigo_grupo']
    valor = grupos_subgrupo_for_departamento(codigo_departamento, grupo)
    subgrupo = []
    for i in valor:
        resultado = {"codigo":None, "Descripcion": None}
        resultado["codigo"] = i.get("c_CODIGO")
        resultado["Descripcion"] = i.get("c_DESCRIPCIO")
        subgrupo.append(resultado)
    
    return jsonify(subgrupo)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



@bp.route('api/depto/v1', methods=['POST'])
def api_dpto_route():
    try:
        data = request.json
        FechaInicio = data['fechaInicio']
        fechaFin = data['fechaFin']
        departamento = data['departamento']
        valores = consulta_departamentos_filtro_tiendas(FechaInicio, fechaFin, departamento)
        
        
        total_cantidad = sum(item["suma_cantidad"] for item in valores)
        total_ventas = sum(item["suma_total"] for item in valores)
        
        
        return jsonify({"Valores_Tienda":valores, "Valores_Ventas_Generales":total_ventas, "Valores_cantidad_General":total_cantidad})
    except Exception as e:
        return jsonify({"Error":str(e)}) , 500




@bp.route('api/depto/v1/grupo', methods=['POST'])
def api_dpto_grupo_route():
    try:
        data = request.json
        FechaInicio = data['fechaInicio']
        fechaFin = data['fechaFin']
        departamento = data['departamento']
        grupo = data["grupo"]
        valores = consulta_departamentos_grupo_filtro_tiendas(FechaInicio, fechaFin, departamento, grupo)
        
        total_cantidad = sum(item["suma_cantidad"] for item in valores)
        total_ventas = sum(item["suma_total"] for item in valores)
        
        return jsonify({"Valores_Tienda":valores, "Valores_Ventas_Generales":total_ventas, "Valores_cantidad_General":total_cantidad})
    except Exception as e:
        return jsonify({"Error":str(e)}) , 500





@bp.route('api/depto/v1/grupo/subgrupo', methods=['POST'])
def api_dpto_grupo_subgrupo_route():
    try:
        data = request.json
        FechaInicio = data['fechaInicio']
        fechaFin = data['fechaFin']
        departamento = data['departamento']
        grupo = data["grupo"]
        sub_grupo = data['subgrupo']
        valores = consulta_departamentos_grupo_subgrupo_filtro_tiendas(FechaInicio, fechaFin, departamento, grupo, sub_grupo)
        
        total_cantidad = sum(item["suma_cantidad"] for item in valores)
        total_ventas = sum(item["suma_total"] for item in valores)
        
        return jsonify({"Valores_Tienda":valores, "Valores_Ventas_Generales":total_ventas, "Valores_cantidad_General":total_cantidad})
    except Exception as e:
        return jsonify({"Error":str(e)}) , 500


