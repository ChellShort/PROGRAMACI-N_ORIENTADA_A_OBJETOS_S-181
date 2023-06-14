#importación del framework
from flask import Flask
from flask_mysqldb import MySQL

#inicialización del framework (app)
app= Flask(__name__)
#ingreso de las credenciales para el acceso a la bd
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='prueba' 
mysql= MySQL(app)


#declaración de la ruta principal (index) http://localhost:5000
@app.route('/')
def index(): #metodo index
    return "Hola mundo Flask" #el metodo index nos regresa un hola mundo

@app.route('/guardar')
def guardar(): #metodo guardar
    return "Se guardo en la BD"

@app.route('/eliminar')
def eliminar(): #metodo eliminar
    return "Se elimino la base de datos"

#ejecución del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)