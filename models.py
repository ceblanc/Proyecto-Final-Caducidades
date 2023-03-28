import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class Producto(db.Base):
    __tablename__ = "producto"
    idProducto = Column(Integer, primary_key=True) #Identificador único de producto
    nombreProducto = Column(String(100), nullable = False)
    referenciaProducto = Column(String(20), nullable = False)
    codigoBarras = Column(Integer, nullable = False)
    marca = Column(String(20), nullable = False)
    proveedor = Column(String(30), nullable = False)
    activo = Column(Boolean)

    def __init__(self,idProducto,nombreProducto,referenciaProducto,codigoBarras,marca,proveedor,activo):
        self.idProducto = idProducto
        self.nombreProducto = nombreProducto
        self.referenciaProducto = referenciaProducto
        self.codigoBarras = codigoBarras
        self.marca = marca
        self.proveedor = proveedor
        self.activo = activo

        def __repr__(self):
            return "Producto {} creado".foprodurmat(self.nombreProducto)

class Fecha(db.Base):
    __tablename__ = "fecha"
    idFecha = Column(Integer, primary_key=True) #Identificador único de fecha
    idProductoFecha = Column(Integer,ForeignKey('producto.idProducto'))
    nombreProductoFecha = Column(String, ForeignKey('producto.nombreProducto'))
    fecha = Column(String(20), nullable = False)
    activoFecha = Column(Boolean)

    def __init__(self,idFecha,idProductoFecha,nombreProductoFecha,fecha,activoFecha):
        self.idFecha = idFecha
        self.idProductoFecha = idProductoFecha
        self.nombreProductoFecha = nombreProductoFecha
        self.fecha = fecha
        self.activoFecha = activoFecha

        def __repr__(self):
            return "Fecha {} registrada".foprodurmat(self.fecha)