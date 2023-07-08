
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL


app= Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_fruteria' 
app.secret_key='mysecretkey'
mysql= MySQL(app)

@app.route('/Consultar_nombre')
def Consultar_nombre():
    return render_template('Consultar_nombre.html')

@app.route('/Buscar', methods=['GET', 'POST'])
def Buscar():
    if request.method == 'POST':
        Vfruta= request.form['txtFruta']
        CC1=mysql.connection.cursor() 
        CC1.execute('SELECT * FROM tbfrutas WHERE fruta = %s', (Vfruta,)) 
        busFrutas=CC1.fetchall()
        return render_template('Consultar_nombre.html', listFrutas=busFrutas)
    return redirect(url_for('Consultar_nombre'))
    

@app.route('/Ingresar_Datos')
def Ingresar_Datos():
    return render_template('Ingresar_Datos.html')

@app.route('/Editar_eliminar')
def Editar_eliminar():
    CC=mysql.connection.cursor() 
    CC.execute('SELECT * FROM tbfrutas')
    conFrutas=CC.fetchall()
    return render_template('Editar_eliminar.html', listFrutas=conFrutas)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vfruta= request.form['txtFruta']
        Vtemporada= request.form['txtTemporada']
        Vprecio= request.form['txtPrecio']
        Vstock= request.form['txtStock']
        CS = mysql.connection.cursor()
        CS.execute('insert into tbfrutas (fruta, temporada, precio, stock) values (%s, %s, %s, %s)',(Vfruta, Vtemporada, Vprecio, Vstock))
        mysql.connection.commit()

    flash('La fruta '+ Vfruta +' fue agregada correctamente')
    return redirect(url_for('Ingresar_Datos'))

@app.route('/editar/<string:id>')
def editar(id):
    cursorID= mysql.connection.cursor()
    cursorID.execute('SELECT * from tbfrutas where id=%s', (id,))
    consulID=cursorID.fetchone()
    return render_template('editarFruta.html', fruta=consulID)

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        varFruta=request.form['txtFruta']
        varTemporada=request.form['txtTemporada']
        varPrecio=request.form['txtAnio']
        varStock=request.form['txtAnio']
        curAct = mysql.connection.cursor()
        curAct.execute('UPDATE tbfrutas set fruta = %s, temporada= %s, precio =%s, stock=%s WHERE id=%s',(varFruta, varTemporada, varPrecio, varStock, id))
        mysql.connection.commit()
    flash('La fruta ' + varFruta + ' fue actualizada correctamente ')
    return redirect(url_for('Editar_eliminar'))

@app.route('/borrar/<id>')
def borrar(id):
    cursorBorrar=mysql.connection.cursor()
    cursorBorrar.execute('DELETE from tbfrutas WHERE id=%s', (id,))
    mysql.connection.commit()
    flash('La fruta fue eliminado')
    return redirect(url_for('Editar_eliminar'))

if __name__ == '__main__':
    app.run(port=5000,debug=True)