import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    caminho = "C:\\Users\\natha\\OneDrive\\Documentos\\projeto\\cadastro_produtos\\banco_de_dados_produtos.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    
    return con

vcon = ConexaoBanco()
print("Conexão estabelecida com sucesso")

vsql = """CREATE TABLE IF NOT EXISTS banco_de_dados_produtos(
        ID_PRODUTO INTEGER PRIMARY KEY AUTOINCREMENT,
        T_NOMEPRODUTO TEXT (30),
        I_CODIGOPRODUTO INTEGER, 
        N_VALOR NUMERIC
)"""

def CriarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print("Tabela Criada")
        conexao.commit() 
    except Error as ex:
        print(ex)

CriarTabela(vcon, vsql)

def CadastrarProduto(conexao):
    produto = input("Digite o produto: ")
    codigo = input("Digite o código do produto: ")
    valor = input("Digite o valor do produto: R$ ")

    vsql = "INSERT INTO banco_de_dados_produtos (T_NOMEPRODUTO, I_CODIGOPRODUTO, N_VALOR) VALUES (?, ?, ?)"
    parametros = (produto, codigo, valor)

    Inserir(conexao, vsql, parametros)

def Inserir(conexao, sql, parametros):
    try:
        c = conexao.cursor()
        c.execute(sql, parametros)
        conexao.commit()
        print('Registro Inserido')
    except sqlite3.Error as ex:
        print(ex)

CadastrarProduto(vcon)


