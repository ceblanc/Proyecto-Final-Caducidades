from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

import db

from models import Producto, Fecha

app = Flask(__name__) #En app se encuentra el servidor web de Flask

#Ruta de la home

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/acciones')
def acciones():
    todos_los_productos = db.session.query(Producto).all() #Consultamos y almacenamos todos los productos de la bbdd
    return render_template("gestion-producto.html", lista_de_productos = todos_los_productos)
@app.route('/caducidades')
def caducidades():
    todas_las_fechas = db.session.query(Fecha).all() #Consultamos y almacenamos todas las fechas de la bbdd
    return render_template("caducidades.html", lista_de_fechas = todas_las_fechas)

@app.route('/caducidades-proximas')
def caducidadesProximas():
    fechas_proximas = db.session.query(Fecha).all() #Consultamos y almacenamos todas las fechas de la bbdd
    return render_template("caducidades-proximas.html", lista_de_fechas_proximas = fechas_proximas)

@app.route('/productos')
def productos():
    return render_template('productos.html')
@app.route('/fechas')
def fechas():
    return render_template('fechas.html')

@app.route('/fechas/crear-fecha/<numProducto>')
def crearFecha(numProducto):
        editFecha = db.session.query(Producto).filter_by(idProducto=numProducto).first()
        return render_template("fechas.html", numProducto=numProducto, editFecha = editFecha)

@app.route('/confirmar-fecha/<numProducto>', methods=['POST'])
def confirmarFecha(numProducto):
    lote = Fecha(idFecha=None, idProductoFecha=request.form['idProductoFecha'],nombreProductoFecha=request.form['nombreProductoFecha'],fecha=request.form['fecha'],activoFecha=True)
    db.session.add(lote)  # Añadir el objeto de Producto a la base de datos
    db.session.commit()  # Ejecutar la operación pendiente de la base de datos
    return redirect(url_for('home')) #Redirección a la página de acciones

@app.route('/eliminar-fecha/<idProductoFecha>')
def eliminarFecha(idProductoFecha):
    #producto = db.session.query(Producto).filter_by(idProducto=int(idProducto))
    productoFecha = db.session.query(Fecha).filter_by(idProductoFecha=idProductoFecha).delete()
    db.session.commit()
    return redirect(url_for('caducidades'))

@app.route('/productos/crear-producto', methods=['POST'])
def crear():
    #producto es un objeto de la clase Producto
    producto=Producto(idProducto=None, nombreProducto=request.form['nombre'],referenciaProducto=request.form['referencia'],codigoBarras=request.form['codigoBarras'],marca=request.form['marca'],proveedor=request.form['proveedor'],activo=True)
    db.session.add(producto) #Añadir el objeto de Producto a la base de datos
    db.session.commit() #Ejecutar la operación pendiente de la base de datos
    return redirect(url_for('productos')) #Redirección a la página de productos

@app.route('/productos/eliminar-producto/<idProducto>')
def eliminar(idProducto):
    producto = db.session.query(Producto).filter_by(idProducto=int(idProducto)).delete()
    db.session.commit()
    return redirect(url_for('acciones'))

@app.route('/editar-producto/<numProducto>')
def editar(numProducto):
    edit = db.session.query(Producto).filter_by(idProducto=numProducto).first()
    return render_template("editar-producto.html", numProducto=numProducto, edit=edit)

@app.route('/confirmar-producto/<numProducto>', methods=['POST'])
def confirmar(numProducto):
    #numProducto = db.session.query(Producto).filter_by(idProducto=int(numProducto)).delete() POSIBLE ERROR COPIA PEGA
    numProducto_alt = Producto(idProducto=None, nombreProducto=request.form['nombre'],referenciaProducto=request.form['referencia'],codigoBarras=request.form['codigoBarras'],marca=request.form['marca'],proveedor=request.form['proveedor'],activo=True)
    db.session.add(numProducto_alt)  # Añadir el objeto de Producto a la base de datos
    db.session.commit()  # Ejecutar la operación pendiente de la base de datos
    #numProducto=Producto(idProducto=None, nombreProducto=request.form['nombre'],referenciaProducto=request.form['referencia'],codigoBarras=request.form['codigoBarras'],marca=request.form['marca'],proveedor=request.form['proveedor'],activo=True)
    #numProducto.verified = True
    #db.session.update(producto) #Añadir el objeto de Producto a la base de datos
    #db.session.commit() #Ejecutar la operación pendiente de la base de datos
    return redirect(url_for('acciones')) #Redirección a la página de acciones

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) #Creación del modelo de datos
    app.run(debug=True) #El debug=True hace que cada vez que reiniciemos el servidor o modifiquemos código, el servidor de Flask se reinicie solo

