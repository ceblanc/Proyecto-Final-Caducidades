import db
from sqlalchemy import Column, Integer, String, Boolean

class Producto(db.Base)
    __tablename__ = "producto"
    idProducto = Column(Integer, primary_key = True) #Identificador único de producto
    nombreProducto = Column(String(100)), nullable = False)
    referenciaProducto = Column(String(20)), nullable = False)
    codigoBarras = Column(Integer(13)), nullable = False)
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
            return "Producto {} creado".format(self.nombreProducto)