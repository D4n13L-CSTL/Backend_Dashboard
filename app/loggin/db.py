# Configuración o modelos del módul
from conexiones.adaptadores_Sqlite import get_db_SAF
from conexiones.adaptadores import get_db_connection_index


def loggin_ps(username):
    db = get_db_connection_index()
    cursor = db.cursor()
    cursor.execute("select id, username, password from usuarios where username = %s", (username,))
    
    data = cursor.fetchall()
    db.close()
    
    return data
