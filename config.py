from psycopg2 import connect

HOST = 'dpg-ck961ff0vg2c738aaa4g-a.oregon-postgres.render.com'

PORT = 5432
BD = 'petshop_3igr'
USUARIO = 'petshop_3igr_user'
PASSWORD = '5pXzGIvkwQ9Ko25aMqxLYD9m3OkKc7mf'

#HOST = 'containers-us-west-140.railway.app'
#PORT = 7824
#BD = 'railway'
#USUARIO = 'postgres'
#PASSWORD = 'Z6zDyduBE98qyCg8ECRE'

def EstablecerConexion():
    try:
        conexion =connect(host=HOST,port=PORT,database=BD, user=USUARIO, password=PASSWORD)
    except ConnectionError:
       print("Error de Conexión")
       
    return conexion 