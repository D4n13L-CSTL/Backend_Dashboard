
import os
import pymssql

import psycopg2


from dotenv import load_dotenv
load_dotenv()

def get_db_connection(): 
    return pymssql.connect(
        server=os.getenv('SERVER'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE')
    )



def get_db_connection_index():#PORT SAF
    return psycopg2.connect(
        host=os.getenv("SERVER_PG"),
        database=os.getenv("DATABASE_PG_SAF"),
        user=os.getenv("USER_PG"),
        password=os.getenv("PASSWORD_PG"),
        port=50250
    )
    
def get_db_connection_resumenes():#PORT RESUMENES
    return psycopg2.connect(
        host=os.getenv("SERVER_PG"),
        database=os.getenv("DATABASE_PG_2020_2023"),
        user=os.getenv("USER_PG"),
        password=os.getenv("PASSWORD_PG"),
        port=50250
    )
    

def get_db_connection_2024():#PORT DB 2024
    return psycopg2.connect(
        host=os.getenv("SERVER_PG"),
        database=os.getenv("DATABASE_PG_2024"),
        user=os.getenv("USER_PG"),
        password=os.getenv("PASSWORD_PG"),
        port=50250
    )

def get_db_connection_deptos():#PORT DEPTOS
    return psycopg2.connect(
        host=os.getenv("SERVER_PG"),
        database=os.getenv("DATABASE_PG_VentasDptos"),
        user=os.getenv("USER_PG"),
        password=os.getenv("PASSWORD_PG"),
        port=50250
    )



