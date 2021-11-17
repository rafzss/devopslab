from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Laboratório DevOps - FIAP 8ASO"

if __name__ == '__main__':
    app.run()