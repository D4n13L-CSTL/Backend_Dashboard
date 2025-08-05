from flask import Flask
import os
from config import settings
from flask_cors import CORS
from app.ajustes.routers import bp as ajustes_bp
from app.api_agentes.routers import bp as api_agentes_bp
from app.auth.routers import bp as auth_bp
from app.deptos.routers import bp as deptos_bp
from app.index.routers import bp as index_bp
from app.inventario.routers import bp as inventario_bp
from app.loggin.routers import bp as loggin_bp
from app.marcas.routers import bp as marcas_bp
from app.meses.routers import bp as meses_bp
from app.rango_fecha.routers import bp as rango_fecha_bp
from app.reposicion.routers import bp as reposicion_bp
from app.resumenes.routers import bp as resumenes_bp
from app.tendencias.routers import bp as tendencias_bp
from app.tiendas.routers import bp as tiendas_bp


def create_app():
    app = Flask(__name__)
    app.config['SESSION_COOKIE_NAME'] = 'session'
    app.config['SECRET_KEY'] = settings.SECRET_KEY
    app.config['DEBUG'] = settings.DEBUG
    CORS(app, supports_credentials=True, origins=["*"])
    app.register_blueprint(ajustes_bp)
    app.register_blueprint(api_agentes_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(deptos_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(inventario_bp)
    app.register_blueprint(loggin_bp)
    app.register_blueprint(marcas_bp)
    app.register_blueprint(meses_bp)
    app.register_blueprint(rango_fecha_bp)
    app.register_blueprint(reposicion_bp)
    app.register_blueprint(resumenes_bp)
    app.register_blueprint(tendencias_bp)
    app.register_blueprint(tiendas_bp)

    return app
