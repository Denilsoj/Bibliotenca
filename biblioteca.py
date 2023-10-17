usuarios = {}


def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    usuarios[nome] = senha
    print("Usuário cadastrado com sucesso!")


def fazer_login():
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    if nome in usuarios and usuarios[nome] == senha:
        print("Login bem-sucedido!")
        return nome
    else:
        print("Nome de usuário ou senha incorretos.")
        return None


def deslogar(usuario_logado):
    print(f"{usuario_logado} foi deslogado com sucesso!")
    return None