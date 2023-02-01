from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database/productos.db',connect_args={'check_same_thread':False}) #Motor que permite manejar la conexión con la base de datos
#Se añade el argumento connect_args para evitar generar varios hilos de ejecución

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()