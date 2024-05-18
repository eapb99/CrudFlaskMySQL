from flask import Flask, render_template, request, redirect, url_for, jsonify
from controller.controllerCarro import *


#Para subir archivo tipo foto al servidor
import os
from werkzeug.utils import secure_filename 


#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app

msg  =''
tipo =''


#Creando mi decorador para el home, el cual retornara la Lista de Carros
@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template('public/layout.html', miData = listaCarros())


#RUTAS
@app.route('/registrar-carro', methods=['GET','POST'])
def addCarro():
    return render_template('public/acciones/add.html')


 
#Registrando nuevo carro
@app.route('/carro', methods=['POST'])
def formAddCarro():
    if request.method == 'POST':
        marca               = request.form['marca']
        modelo              = request.form['modelo']
        year                = request.form['year']
        color               = request.form['color']
        puertas             = request.form['puertas']
        favorito            = request.form['favorito']
        cilindraje            = request.form['cilindraje']
        velocidad            = request.form['velocidad']
        
        
        if(request.files['foto'] !=''):
            file     = request.files['foto'] #recibiendo el archivo
            nuevoNombreFile = recibeFoto(file) #Llamado la funcion que procesa la imagen
            resultData = registrarCarro(marca, modelo, year, color, puertas, favorito, nuevoNombreFile,cilindraje,velocidad)
            if(resultData ==1):
                return render_template('public/layout.html', miData = listaCarros(), msg='El Registro fue un éxito', tipo=1)
            else:
                return render_template('public/layout.html', msg = 'Metodo HTTP incorrecto', tipo=1)   
        else:
            return render_template('public/layout.html', msg = 'Debe cargar una foto', tipo=1)
            


@app.route('/form-update-carro/<string:id>', methods=['GET','POST'])
def formViewUpdate(id):
    if request.method == 'GET':
        resultData = updateCarro(id)
        if resultData:
            return render_template('public/acciones/update.html',  dataInfo = resultData)
        else:
            return render_template('public/layout.html', miData = listaCarros(), msg='No existe el carro', tipo= 1)
    else:
        return render_template('public/layout.html', miData = listaCarros(), msg = 'Metodo HTTP incorrecto', tipo=1)          
 
   
  
@app.route('/ver-detalles-del-carro/<int:idCarro>', methods=['GET', 'POST'])
def viewDetalleCarro(idCarro):
    msg =''
    if request.method == 'GET':
        resultData = detallesdelCarro(idCarro) #Funcion que almacena los detalles del carro
        
        if resultData:
            return render_template('public/acciones/view.html', infoCarro = resultData, msg='Detalles del Carro', tipo=1)
        else:
            return render_template('public/acciones/layout.html', msg='No existe el Carro', tipo=1)
    return redirect(url_for('inicio'))
    

@app.route('/actualizar-carro/<string:idCarro>', methods=['POST'])
def formActualizarCarro(idCarro):
    if request.method == 'POST':
        # Obtener datos del formulario
        marca = request.form['marca']
        modelo = request.form['modelo']
        year = request.form['year']
        color = request.form['color']
        puertas = request.form['puertas']
        favorito = request.form['favorito']
        cilindraje = request.form['cilindraje']
        velocidad = request.form['velocidad']

        # Obtener datos actuales del carro desde la base de datos
        carroActual = detallesdelCarro(idCarro)
        if not carroActual:
            return render_template('public/layout.html', miData=listaCarros(), msg='Carro no encontrado', tipo=0)

        # Verificar si se ha subido una nueva foto
        if 'foto' in request.files and request.files['foto'].filename != '':
            file = request.files['foto']
            fotoForm = recibeFoto(file)
        else:
            fotoForm = carroActual['foto']  # Mantener la foto existente

        # Actualizar datos del carro
        resultData = recibeActualizarCarro(marca, modelo, year, color, puertas, favorito, fotoForm, cilindraje, velocidad, idCarro)

        # Verificar si la actualización fue exitosa
        if resultData == 1:
            return render_template('public/layout.html', miData=listaCarros(), msg='Datos del carro actualizados', tipo=1)
        else:
            return render_template('public/layout.html', miData=listaCarros(), msg='No se pudo actualizar', tipo=0)

  

#Eliminar carro
@app.route('/borrar-carro', methods=['GET', 'POST'])
def formViewBorrarCarro():
    if request.method == 'POST':
        idCarro         = request.form['id']
        nombreFoto      = request.form['nombreFoto']
        resultData      = eliminarCarro(idCarro, nombreFoto)

        if resultData ==1:
            return jsonify([1])
        else: 
            return jsonify([0])



def recibeFoto(file):
    print(file)
    basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
    filename = secure_filename(file.filename) #Nombre original del archivo

    #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
    extension           = os.path.splitext(filename)[1]
    nuevoNombreFile     = stringAleatorio() + extension
    #print(nuevoNombreFile)
        
    upload_path = os.path.join (basepath, 'static/assets/fotos_carros', nuevoNombreFile) 
    file.save(upload_path)

    return nuevoNombreFile

       
  
  
#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('inicio'))
    
    
    
    
if __name__ == "__main__":
    app.run(debug=True, port=8000)