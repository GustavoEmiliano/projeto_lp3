from flask import Flask

app = Flask("Minha App")

# Uma página do flask é igual a: rota + função
 
#/ home page - Home 
@app.route("/")

def home():
    return "<h1> Home Page </h1>"

#/ contato - página de contato
@app.route("/contato")

def contato():
    return "<h1> Contato </h1>"

#/produtos - pagina produtos
@app.route("/produtos")

def produto():
    return "<h1> Produtos Legais</h1>"
