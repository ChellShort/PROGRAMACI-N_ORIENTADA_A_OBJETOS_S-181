#importación del framework
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

#inicialización del framework (app)
app= Flask(__name__)
#ingreso de las credenciales para el acceso a la bd
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_fruteria' 
app.secret_key='mysecretkey'
mysql= MySQL(app)

#declaración de la ruta principal (index) http://localhost:5000
@app.route('/')
def index(): #metodo index
    #hacer la consulta para mostrar una vista junto con la renderización
    CC=mysql.connection.cursor() 
    CC.execute('SELECT * FROM tbfrutas')  #nuevo (aqui esta nuestra secuencia sql)
    conFrutas=CC.fetchall() #nuevo (devuelve los valores de la secuencia sql)
    #print(conAlbums) #nuevo (se iprime en consola el contendio de la tabla)
    return render_template('index.html', listFrutas=conFrutas) #el metodo index nos lleva a index.html

#ruta http://localhost:5000/guardar tipo POST para Insert
@app.route('/guardar', methods=['POST']) #recibira infor por formulario mediante post
def guardar(): #metodo guardar
    if request.method == 'POST':
        # pasamos a variables el contenido de los input
        Vfruta= request.form['txtFruta']
        Vtemporada= request.form['txtTemporada']
        Vprecio= request.form['txtPrecio']
        Vstock= request.form['txtStock']
        # print(titulo, artista, anio)
        # en lugar de imprimirlo vamos a procesarlo para mandarlo a la base de datos
        # Conectar y ejecutar el insert
        CS = mysql.connection.cursor() # objeto de tipo cursor
        CS.execute('insert into tbfrutas (fruta, temporada, precio, stock) values (%s, %s, %s, %s)',(Vfruta, Vtemporada, Vprecio, Vstock))
        mysql.connection.commit()

    flash('El album fue agregado correctamente')
    return redirect(url_for('index'))


@app.route('/eliminar')
def eliminar(): #metodo eliminar
    return "Se elimino la base de datos"

#ejecución del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)