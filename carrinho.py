import livros
carrinho = {}

def adicionar_ao_carrinho(usuario):
    print("Livros disponíveis para compra:")
    for livro, preco in livros.livros.items():
        print(f"{livro}: R${preco}")
    
    livro_selecionado = input("Digite o nome do livro que deseja adicionar ao carrinho: ")
    if livro_selecionado in livros.livros:
        if usuario not in carrinho:
            carrinho[usuario] = []
        carrinho[usuario].append(livro_selecionado)
        print("Livro adicionado ao carrinho com sucesso!")
    else:
        print("Livro não encontrado.")


def remover_do_carrinho(usuario):
    if usuario in carrinho and len(carrinho[usuario]) > 0:
        print("Livros no carrinho de compras:")
        for i, livro in enumerate(carrinho[usuario]):
            print(f"{i + 1}: {livro}")
        
        escolha = input("Digite o número do livro que deseja remover (ou '0' para cancelar) ou 'v' para ver todos os itens no carrinho: ")
        
        if escolha.lower() == 'v':
            print(f"Carrinho de {usuario}: {', '.join(carrinho[usuario])}")
        elif escolha.isdigit():
            escolha = int(escolha)
            if escolha >= 1 and escolha <= len(carrinho[usuario]):
                livro_removido = carrinho[usuario].pop(escolha - 1)
                print(f"{livro_removido} foi removido do carrinho.")
            else:
                print("Escolha inválida.")
        else:
            print("Operação cancelada.")
    else:
        print("Carrinho de compras vazio.")


def ver_carrinho(usuario):
    if usuario in carrinho:
        total = sum([livros.livros[livro] for livro in carrinho[usuario]])
        print(f"Carrinho de {usuario}: {', '.join(carrinho[usuario])}")
        print(f"Total: R${total}")
    else:
        print(f"Carrinho de {usuario} está vazio.")
