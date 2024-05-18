
# CRUD con MySQL y Flask

Este proyecto es un ejemplo básico de cómo implementar un CRUD (Create, Read, Update, Delete) utilizando MySQL como base de datos y Flask como framework web en Python. El proyecto incluye la configuración del entorno virtual, la conexión a la base de datos y la creación de una tabla con datos de ejemplo.

## Requisitos

- Python 3.7.9
- MySQL

## Configuración del Entorno

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/usuario/mi-proyecto-crud.git
   cd mi-proyecto-crud
   ```

2. **Crear un entorno virtual**

   ```bash
   python3.7 -m venv venv
   ```

3. **Activar el entorno virtual**

   - En Windows:

     ```bash
     venv\Scripts\activate
     ```

   - En MacOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Instalar las dependencias**

   ```bash
   pip install -r requirements.txt
   ```

## Configuración de la Base de Datos

1. **Crear la tabla**

   El archivo `Tabla_carros.sql` contiene las instrucciones SQL necesarias para crear la tabla y algunos datos de ejemplo.


## Conexión a la Base de Datos

El archivo `conexionDB.py` contiene la lógica para conectarse a la base de datos MySQL. Asegúrate de actualizar las credenciales de la base de datos en este archivo:

```python
import mysql.connector

def connectionBD():
    mydb = mysql.connector.connect(
        host ="127.0.0.1",
        user ="user",
        passwd ="",
        database = "crud_flask_python"
        )
    if mydb:
        print ("Conexion exitosa a BD")
        return mydb
    else:
        print("Error en la conexion a BD")
```

## Ejecución de la Aplicación

Para ejecutar la aplicación Flask, utiliza el siguiente comando:

```bash
flask run
```

En Windows, utiliza `set` en lugar de `export`:

La aplicación debería estar disponible en `http://127.0.0.1:5000/`.

## Archivos del Proyecto

- `app.py`: Archivo principal de la aplicación Flask.
- `conexionDB.py`: Archivo que contiene la conexión a la base de datos MySQL.
- `Tabla_carros.sql`: Archivo SQL para crear la tabla e insertar datos de ejemplo.
- `templates/`: Directorio que contiene las plantillas HTML.
- `static/`: Directorio que contiene archivos estáticos como CSS y JavaScript.
- `controller/`: Directorio que contiene el archivo que maneja la conexión a base de las diferentes operacion CRUD.


## Notas

- Asegúrate de tener MySQL en funcionamiento antes de ejecutar la aplicación.
- Ajusta las configuraciones en `conexionBD.py` según tu entorno.
