# Configuración o modelos del módulo
from conexiones.adaptadores_Sqlite import get_db_SAF
from conexiones.adaptadores import get_db_connection_index
import bcrypt

def create_users(nombre_apellido, username, password, email, cargo):
    conn = get_db_connection_index()
    cursor = conn.cursor()

    password_hashear = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    cursor.execute(
        "INSERT INTO usuarios (nombre_apellido, username, password, email, cargo) VALUES (%s, %s, %s, %s, %s)",
        (nombre_apellido, username, password_hashear, email, cargo)
    )

    conn.commit()
    conn.close()




def update_users(campo,dato,id_users):
    conn = get_db_SAF()
    cursor = conn.cursor()
    if campo == "password":
        dato = bcrypt.hashpw(dato.encode('utf-8'), bcrypt.gensalt())
    else :
        dato = dato.upper()
    cursor.execute(f"UPDATE USUARIOS SET {campo} = ? WHERE id = ?",(dato , id_users))
    conn.commit()
    conn.close()
    


def delete_users(username):
    conn = get_db_SAF()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM USUARIOS WHERE username = ?", (username.upper(),))
    conn.commit()
    conn.close()
    

