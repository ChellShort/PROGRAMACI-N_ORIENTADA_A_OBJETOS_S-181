#importación del framework
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

#inicialización del framework (app)
app= Flask(__name__)
#ingreso de las credenciales para el acceso a la bd
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='prueba' 
app.secret_key='mysecretkey'
mysql= MySQL(app)

#declaración de la ruta principal (index) http://localhost:5000
@app.route('/')
def index(): #metodo index
    #hacer la consulta para mostrar una vista junto con la renderización
    CC=mysql.connection.cursor() 
    CC.execute('SELECT * FROM tb_albums')  #nuevo (aqui esta nuestra secuencia sql)
    conAlbums=CC.fetchall() #nuevo (devuelve los valores de la secuencia sql)
    #print(conAlbums) #nuevo (se iprime en consola el contendio de la tabla)
    return render_template('index.html', listAlbums=conAlbums) #el metodo index nos lleva a index.html

#ruta http://localhost:5000/guardar tipo POST para Insert
@app.route('/guardar', methods=['POST']) #recibira infor por formulario mediante post
def guardar(): #metodo guardar
    if request.method == 'POST':
        # pasamos a variables el contenido de los input
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']
        # print(titulo, artista, anio)
        # en lugar de imprimirlo vamos a procesarlo para mandarlo a la base de datos
        # Conectar y ejecutar el insert
        CS = mysql.connection.cursor() # objeto de tipo cursor
        CS.execute('insert into tb_albums (titulo, artista, anio) values (%s, %s, %s)',(Vtitulo, Vartista, Vanio))
        mysql.connection.commit()

    flash('El album fue agregado correctamente')
    return redirect(url_for('index'))

#------------------------------------------------------------
@app.route('/editar/<string:id>')
def editar(id): #metodo editar
    cursorID= mysql.connection.cursor()
    cursorID.execute('SELECT * from tb_albums where id=%s', (id,))
    consulID=cursorID.fetchone()
    return render_template('editarAlbum.html', album=consulID)

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id): #metodo actualizar
    if request.method == 'POST':
        varTitulo=request.form['txtTitulo']
        varArtista=request.form['txtArtista']
        varAnio=request.form['txtAnio']

        curAct = mysql.connection.cursor() # objeto de tipo cursor
        curAct.execute('UPDATE tb_albums set titulo = %s, artista = %s, anio =%s WHERE id=%s',(varTitulo, varArtista, varAnio, id))
        mysql.connection.commit()
    flash('El album fue actualizado correctamente ' + varTitulo)
    return redirect(url_for('index'))
#------------------------------------------------------------

@app.route('/eliminar')
def eliminar(): #metodo eliminar
    return "Se elimino la base de datos"

#ejecución del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)