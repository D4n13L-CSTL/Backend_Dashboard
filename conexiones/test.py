from adaptadores import get_db_connection, get_db_connection_2024,get_db_connection_deptos,get_db_connection_index,get_db_connection_resumenes  # Asegúrate de que este archivo se llama db.py o ajusta el import


def probar_conexion():
    conn = get_db_connection_resumenes()
    if conn:
        print("✅ Conexión exitosa a la base de datos.")
        conn.close()
    else:
        print("❌ No se pudo conectar a la base de datos.")





if __name__ == "__main__":
    pass