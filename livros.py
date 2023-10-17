livros = {}

def cadastrar_livro():
    nome_livro = input("Digite o nome do livro: ")
    preco = float(input("Digite o preço do livro: "))
    livros[nome_livro] = preco
    print("Livro cadastrado com sucesso!")




def apagar_livro():
    livro = input("Digite o nome do livro que deseja apagar: ")
    if livro in livros:
        del livros[livro]
        print(f"Livro '{livro}' foi apagado da lista de livros.")
    else:
        print("Livro não encontrado.")