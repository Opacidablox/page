from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    
    <h1>Hello, World!</h1>
        <ul>
        <li>
        <a href="/numeros">Dar click para ver numeros aleatorios</a>
        </li>
        <li>
        <a href="/datos">Dar click para ver datos aleatorios</a>
        </li>
        <li>
        <a href="/suma/1/1">Dar click para ver la suma de dos números (escribelos en la URL)</a>
        </li>
        <li>
        <a href="/contraseña">Dar click para generar una contraseña</a>
        </li>
    </ul>
    
    """

@app.route("/numeros")
def numeros():
    num = random.randint(1,100)
    return f"<h1> El numero es {num} </h1>"

@app.route("/datos")
def datos():
    datos = [
        "Jupiter es el planeta mas grande del sistema solar",
        "los ornitorrincos sudan leche 🙏",
        "El Sol es de color blanco ",
        "La capital de Colombia es Bogota"
    ]
    return f"<h1> Aquí tienes un dato random: {random.choice(datos)} </h1>"

@app.route("/suma/<int:n1>/<int:n2>")
def suma(n1:int,n2:int):
    return f" <h1>La suma de {n1} con {n2} es {n1 + n2} </h1>"

@app.route("/contraseña")
def contraseña():
    letters = "QWERTYUIOPASDFGHJKLÑZXCVBNMqwertyuiopasdfghjklñzxcvbnm1234567890!#$%&/()='¿?¡<>-_+*@"
    word = ""
    for i in range(12):
        word += random.choice(letters)
    return f"<h1> Aquí tienes una contraseña: {word} </h1>"

app.run(debug=True)
