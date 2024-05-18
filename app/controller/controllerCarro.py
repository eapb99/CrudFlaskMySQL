from random import sample
from conexionBD import *  #Importando conexion BD
import os


#Creando una funcion para obtener la lista de carros.
def listaCarros():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM carros ORDER BY id DESC"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda




def updateCarro(id=''):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM carros WHERE id = %s LIMIT 1", [id])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData
    
    
    
def registrarCarro(marca='', modelo='', year='', color='', puertas='', favorito='', nuevoNombreFile='',cilindraje='',velocidad=''):       
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
            
        sql         = ("""INSERT INTO carros(marca, modelo, year, color, puertas, favorito, foto, cilindraje, velocidad) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s)""")
        valores     = (marca, modelo, year, color, puertas, favorito, nuevoNombreFile,cilindraje,velocidad)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        resultado_insert = cursor.rowcount #retorna 1 o 0
        ultimo_id        = cursor.lastrowid #retorna el id del ultimo registro
        return resultado_insert
  
def detallesdelCarro(idCarro):
        try:
                conexion_MySQLdb = connectionBD()
                with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                        cursor.execute("SELECT * FROM carros WHERE id = %s", (idCarro,))
                        resultadoQuery = cursor.fetchone()
                        return resultadoQuery
        except Exception as e:
                print(f"Error: {e}")
                return None
        finally:
                conexion_MySQLdb.close()
    
    

def  recibeActualizarCarro(marca, modelo, year, color, puertas, favorito, nuevoNombreFile, cilindraje, velocidad, idCarro):
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        print(idCarro)
        cur.execute("""
            UPDATE carros
            SET 
                marca   = %s,
                modelo  = %s,
                year    = %s,
                color   = %s,
                puertas = %s,
                favorito= %s,
                foto    = %s,
                cilindraje    = %s,
                velocidad    = %s
            WHERE id=%s
            """, (marca,modelo, year, color, puertas, favorito, nuevoNombreFile, cilindraje, velocidad, idCarro))
        conexion_MySQLdb.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        resultado_update = cur.rowcount #retorna 1 o 0
        print(resultado_update)
        return resultado_update
 


def eliminarCarro(idCarro='', nombreFoto=''):
    try:
        basepath = os.path.dirname(__file__)  
        app_path = os.path.abspath(os.path.join(basepath, '..'))

        url_File = os.path.join(app_path, 'static', 'assets', 'fotos_carros', nombreFoto)
        url_File_normalized = os.path.normpath(url_File)
        # Verificar si la foto existe
        if not os.path.exists(url_File) :
            print(f"La foto {nombreFoto} no se encontró en el sistema de archivos")
            return 0  # Indicar que no se eliminó el registro porque la foto no existe

        # Conexión a la base de datos
        conexion_MySQLdb = connectionBD()  # Hago instancia a mi conexión desde la función
        cur = conexion_MySQLdb.cursor(dictionary=True)

        # Eliminar carro de la base de datos
        cur.execute('DELETE FROM carros WHERE id=%s', (idCarro,))
        conexion_MySQLdb.commit()
        resultado_eliminar = cur.rowcount  # Retorna 1 o 0

        # Verificar si se eliminó el registro
        if resultado_eliminar == 0:
            print("No se encontró un carro con el id proporcionado")
            return 0  # Indicar que no se eliminó el registro porque no se encontró

        # Eliminar foto del sistema de archivos
        os.remove(url_File)  # Borrar foto desde la carpeta
        return 1  # Indicador de éxito

    except Exception as e:
        # Manejo de excepciones
        print(f"Error al eliminar el carro: {e}")
        return 0  # Indicador de fallo

    finally:
        # Asegurarse de cerrar la conexión a la base de datos
        if 'cur' in locals():
            cur.close()
        if 'conexion_MySQLdb' in locals():
            conexion_MySQLdb.close()

#Crear un string aleatorio para renombrar la foto 
# y evitar que exista una foto con el mismo nombre
def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio