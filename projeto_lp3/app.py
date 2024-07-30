from flask import Flask, render_template, request
from validate_docbr import CPF
from validate_docbr import CNPJ

lista_produtos = [
        {"nome" : "Coca-Cola", "descricao" : "Mata a sede", "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQm4S15squn95k7qtrVOpMX1MOJGe48y4B7FQ&s"},
        {"nome" : "Doritos", "descricao" : "Suja a mão", "url": "https://atacadaobr.vtexassets.com/arquivos/ids/252509/g.jpg?v=638353972719200000"},
        {"nome" : "Chocolate", "descricao" : "Bom", "url" : "https://www.havan.com.br/media/catalog/product/cache/73a52df140c4d19dbec2b6c485ea6a50/b/a/barra-de-chocolate-ao-leite-nestle_806102.jpg"},
]

cnpj = CNPJ()
cpf = CPF()
app = Flask("Minha App")

# Uma página do flask é igual a: rota + função
 
#/ home page - Home 
@app.route("/")
def home():
    return render_template("home.html")

#/ contato - página de contato
@app.route("/contato")
def contato():
    return render_template("contato.html")

#/produtos - pagina produtos
@app.route("/produto")
def produtos():
   
    return render_template("produto.html", produtos = lista_produtos)




#/produtos - pagina servicos
@app.route("/servicos")
def servicos():
    return render_template("servicos.html")

#/produtos - pagina gerar-cpf
@app.route("/gerar-cpf")
def gerarcpf():
    # cpfs = []
    # for i in range(10):
    #     cpfs.append(cpf.generate(True))
    
        
    return render_template("cpf.html", gerarcpf = cpf.generate_list(n=20))

@app.route("/gerar-cnpj")
def gerarcnpj():
    cnpjs = []   

    for i in range(10):
        cnpjs.append(cpf.generate(True))
        
    return render_template("cnpj.html", gerarcnpj = cnpjs)

@app.route("/enviado")
def Enviado():
    return render_template("enviado.html")

@app.route("/ComoUsar")
def ComoUsar():
    return render_template("ComoUsar.html")
    

@app.route("/Privacidade")
def Privacidade():
    return render_template("privacidade.html")

@app.route("/Termos")
def Termos():
    return render_template("termos.html")
    

#pagina/ servicos retornar "Nosso serviços"
#pagina/ gerar-cpf retornar cpf aleatorio
#pagina/ gerar-cnpj retornar cnpj aleatorio


## GET/produtos/cadastros/devolver o form
@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

# POST/produto que vai lidar com os dados enviados pelo form
#   acessar o objeto request(foi importado do lado de flask)
@app.route("/produto", methods = ["POST"])
def salvar_produto():
    #pegando os valores digitados no form
    #que estão na request
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    
    #crio um novo dictionary/produto
    produto = {"nome": nome, "descricao": descricao, "url": ""}
    
    #adiciona na lista esse novo produto
    lista_produtos.append(produto)
    
    #retorna o template já com o novo produto cadastrado
    return render_template("produto.html", produtos = lista_produtos)


@app.route("/produtos/<nome>/excluir")
def excluir_produto(nome):
    # logica de exclusao
    return "Produto excluido " + nome

app.run(debug=True)