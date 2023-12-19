senha: str
senha_correta: str
login: str
login_correto: str

login_correto = "funcionaria@acesso.com"
senha_correta = "2002"

login = input('Email: ')
senha = input('Senha: ')

if login == login_correto and senha == senha_correta:
    print("Acesso Permitido. ")
    print("Bem-vindo ao sistema!")
else:
    print('Acesso Negado!')
    print("Email ou senha inválida. Tente novamente.")