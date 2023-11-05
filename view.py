import sqlite3 as banco

# Criando a conexão
bd = banco.connect('dados.db')

lista = []

# ------ CRUD ----- #

# Create
def adicionarProduto(i):
    """Esta função exibe informações sobre os produtos."""
    with bd:
        cursor = bd.cursor()
        query = "INSERT INTO Produtos (nome, data_compra, valor, metodo_pagamento, descricao, status_despesa) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(query,i)

# Read
def exibirProduto():
    lista = []
    with bd:
        cursor = bd.cursor()
        query = "SELECT * FROM Produtos"
        cursor.execute(query)
        info = cursor.fetchall()
        for i in info:
          lista.append(i)
    return info

# Update
def atualizarProduto(i):
    with bd:
        cursor = bd.cursor()
        query = "UPDATE Produtos SET nome=?, data_compra=?, valor=?, metodo_pagamento=?, descricao=?, status_despesa=? WHERE id=?"
        cursor.execute(query, i)


# Delete
def deletarProduto(id):
    with bd:
        cursor = bd.cursor()
        query = "DELETE FROM Produtos WHERE id=?"
        cursor.execute(query, (id,))
