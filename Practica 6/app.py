#importación del framework
from flask import Flask,render_template,request
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
    return render_template('index.html') #el metodo index nos lleva a index.html

#ruta http://localhost:5000/guardar tipo POST para Insert
@app.route('/guardar', methods=['POST']) #recibira infor por formulario mediante post
def guardar(): #metodo guardar
    if request.method == 'POST':
        titulo= request.form['txtTitulo']
        artista= request.form['txtArtista']
        anio= request.form['txtAnio']
        print(titulo, artista, anio)
    return 'Los datos llegaron'

@app.route('/eliminar')
def eliminar(): #metodo eliminar
    return "Se elimino la base de datos"

#ejecución del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)