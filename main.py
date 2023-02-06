from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) #En app se encuentra el servidor web de Flask

#Ruta de la home

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/informes')
def informes():
    return render_template("informes.html")

@app.route('/articulos')
def articulos():
    return render_template('articulos.html')
@app.route('/fechas')
def fechas():
    return render_template('fechas.html')

if __name__ == '__main__':
    app.run(debug=True) #El debug=True hace que cada vez que reiniciemos el servidor o modifiquemos código, el servidor de Flask se reinicie solo

