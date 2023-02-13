from flask import Flask, render_template, request, url_for
import db

from models import Producto

app = Flask(__name__) #En app se encuentra el servidor web de Flask

#Ruta de la home

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/informes')
def informes():
    todos_los_productos = db.session.query(Producto).all() #Consultamos y almacenamos todos los productos de la bbdd
    return render_template("informes.html", lista_de_productos = todos_los_productos)

@app.route('/productos')
def productos():
    return render_template('productos.html')
@app.route('/fechas')
def fechas():
    return render_template('fechas.html')

@app.route('/productos/crear-producto', methods=['POST'])
def crear():
    #producto es un objeto de la clase Producto
    producto=Producto(idProducto=None, nombreProducto=request.form['nombre'],referenciaProducto=request.form['referencia'],codigoBarras=request.form['codigoBarras'],marca=request.form['marca'],proveedor=request.form['proveedor'],activo=True)
    db.session.add(producto) #Añadir el objeto de Producto a la base de datos
    db.session.commit() #Ejecutar la operación pendiente de la base de datos
    return "Producto creado"

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) #Creación del modelo de datos
    app.run(debug=True) #El debug=True hace que cada vez que reiniciemos el servidor o modifiquemos código, el servidor de Flask se reinicie solo

