import sqlite3 as banco

# Criando a conexão
bd = banco.connect('dados.db')

# Tabela
with bd:
    cursor = bd.cursor()
    cursor.execute("CREATE TABLE Produtos(id INTEGER PRIMARY KEY, nome TEXT, data_compra DATE, valor FLOAT, metodo_pagamento TEXT, descricao TEXT, status_despesa TEXT)")
