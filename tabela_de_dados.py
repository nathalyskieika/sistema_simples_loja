import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    caminho = 'C:\\python teste\\banco_de_dados\\dados.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vsql = """CREATE TABLE IF NOT EXISTS dados (
            T_IDENTIFICACAO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOME TEXT(30),
            T_NASCIMENTO TEXT(20),
            T_TELEFONE TEXT(20),
            T_EMAIL TEXT(20),
            T_CPF TEXT(20),
            T_GENERO TEXT(20)
);"""

def CriarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print("Tabela Criada")
        conexao.commit()  # Certifique-se de fazer o commit
    except Error as ex:
        print(ex)

vcon = ConexaoBanco()
CriarTabela(vcon, vsql)

def InserirDado(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except sqlite3.Error as ex:
        print(ex)

def BuscarCliente(conexao, cpf):
    cursor = conexao.cursor()
    cursor.execute('''
                    SELECT * FROM dados
                    WHERE T_CPF LIKE ?
                    ''', ('%' + cpf + '%',))
    dados_cliente = cursor.fetchall()
    return dados_cliente 

def CadastrarCliente(conexao):
    nome = input("Digite o nome: ")
    nascimento = input("Digite a data de nascimento: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    cpf = input("Digite o CPF: ")
    genero = input("Digite o genero: ")
    vsql = f"INSERT INTO dados (T_NOME, T_NASCIMENTO, T_TELEFONE, T_EMAIL, T_CPF, T_GENERO) " \
           f"VALUES('{nome}','{nascimento}','{telefone}','{email}','{cpf}','{genero}')"
    InserirDado(vcon, vsql)  
    print("Cliente registrado com sucesso!")

vcon = ConexaoBanco()
cursor = vcon.cursor()
