from flask import Flask, jsonify, request
from database import db

app = Flask(__name__)

@app.route('/produtos', methods=["GET"])
def get_produtos():
  produtos = db["produtos"]
  return jsonify(produtos)

@app.route('/produtos/<int:id>', methods=["GET"])
def get_produto_id(id):
  lista_produtos = db["produtos"]
  for produto in lista_produtos:
    if produto["id"] == id:
      return jsonify(produto)
  return jsonify({"erro":"produto não encontrado"}), 404

@app.route('/produtos', methods=["POST"])
def create_produto():
    novo_produto = request.json
    db["produtos"].append(novo_produto)
    return jsonify(novo_produto), 201
  
@app.route('/produtos/<int:id>', methods=["PUT"])
def update_produto(id):
  lista_produtos = db["produtos"]
  dados = request.json
  for produto in lista_produtos:
    if produto["id"] == id:
      produto.update({
        "nome": dados.get("nome", produto["nome"]),
        "descricao": dados.get("descricao", produto["descricao"]),
        "categoria": dados.get("categoria", produto["categoria"]),
        "preco_unitario": dados.get("preco_unitario", produto["preco_unitario"]),
        "quantidade_estoque": dados.get("quantidade_estoque", produto["quantidade_estoque"]),
        "id_fornecedor": dados.get("id_fornecedor", produto["id_fornecedor"]) 
      })
      return jsonify(produto), 200
  return jsonify({"erro": "produto não encontrado"}), 404

@app.route('/produtos/<int:id>', methods=["PUT"])
def delete_produto(id):
  lista_produtos = db["produtos"]
  for produto in lista_produtos:
    if produto[id] == id:
      produto.remove(lista_produtos)
      db["produtos"] = lista_produtos
      return jsonify(db["produtos"])
  return jsonify({"erro": "produto não encontrado"})
  
''' exemplo para testar o post
{
  "id": 2,
  "nome": "Teclado RGB",
  "descricao": "Teclado mecânico com luz",
  "categoria": "Periférico",
  "preco_unitario": 199.99,
  "quantidade_estoque": 10,
  "id_fornecedor": 2
}
'''
  
if __name__ == '__main__':
    app.run(debug=True)


