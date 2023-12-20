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

# Criar Tabela
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

buscar_sim = 'sim'
buscar_nao = 'nao'
pesquisar_sim = 'sim'
pesquisar_nao = 'nao'

pesquisar = input("Pesquisar cliente? ")

if pesquisar == pesquisar_sim:
    buscar = input("Digite o CPF: ")
    dados_cliente = BuscarCliente(vcon, buscar)

    if dados_cliente:
        print("Cliente encontrado.")
        for cliente in dados_cliente:
            print("Nome:", cliente[1])
            print("Nascimento:", cliente[2])
            print("Telefone:", cliente[3])
            print("Email:", cliente[4])
            print("CPF:", cliente[5])
            print("Genero:", cliente[6])
    else:
        print("Cliente não encontrado.")
        cadastrar_novo = input("Deseja cadastrar um novo cliente? (sim/nao) ").lower()
        if cadastrar_novo == 'sim':
            CadastrarCliente(vcon)
        else:
            print("Pesquisa Cancelada.")
elif pesquisar == pesquisar_nao:
    print("Pesquisa cancelada.")
else:
    print("Opção inválida.")

vcon.close()

