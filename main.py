from flask import Flask

app = Flask(__name__) #En app se encuentra el servidor web de Flask

#Ruta de la home

@app.route('/')
def home():
    return 'NOMBRE'

if __name__ == '__main__':
    app.run(debug=True) #El debug=True hace que cada vez que reiniciemos el servidor o modifiquemos código, el servidor de Flask se reinicie solo

