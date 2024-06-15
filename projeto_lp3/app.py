from flask import Flask
from validate_docbr import CPF, CNPJ

cpf = CPF()
cnpj = CNPJ()

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

# Abaixo está o exercicio sobre rotas, praticado em aula de reposição.

# página/servicos retornar "Nossos Serviços"
# pagina /gerar-cpf retornar Cpf Aleatorio
# pagina /gerar-cnpj retornar Cnpj aleatório


# /servicos - pagina serviços

@app.route("/servicos")
def servicos():
    return "<h1> Nossos Serviços </h1>"


@app.route("/gerar-cpf")
def gerar_cpf():
    return f"CPF: {cpf.generate(True)}"

@app.route("/gerar-cnpj")
def gerar_cnpj():
    return f"CNPJ: {cnpj.generate(True)}"

@app.route("/gerar-5-cpfs")
def gerar_5_cpfs():
    cpfs = []
    for i in range(5):
        cpfs.append(cpf.generate(True))
    return  f'CPFS: {cpfs} '

@app.route("/gerar-5-cnpjs")
def gerar_5_cnpjs():
    cnpjs = []
    for i in range(5):
        cnpjs.append(cnpj.generate(True))
    return  f'CNPJS: {cnpjs} '

app.run(debug=True)