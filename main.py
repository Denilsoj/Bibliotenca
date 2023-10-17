import biblioteca
import carrinho
import livros

usuario_logado = None

while True:
    print("\nBiblioteca Online")
    print("1. Cadastrar usuário")
    
    if usuario_logado is None:
        print("2. Fazer login")
    else:
        print(f"2. Deslogar (Logado como {usuario_logado})")
    
    print("3. Cadastrar livro")
    print("4. Adicionar livro ao carrinho")
    print("5. Remover livro do carrinho")
    print("6. Ver carrinho e valor total")
    print("7. Apagar livro da lista de livros")
    print("8. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        biblioteca.cadastrar_usuario()
    elif escolha == "2":
        if usuario_logado is None:
            usuario_logado = biblioteca.fazer_login()
        else:
            usuario_logado = biblioteca.deslogar(usuario_logado)
    elif escolha == "3":
        if usuario_logado:
            livros.cadastrar_livro()
        else:
            print("Faça o login primeiro.")
    elif escolha == "4":
        if usuario_logado:
            carrinho.adicionar_ao_carrinho(usuario_logado)
        else:
            print("Faça o login primeiro.")
    elif escolha == "5":
        if usuario_logado:
            carrinho.remover_do_carrinho(usuario_logado)
        else:
            print("Faça o login primeiro.")
    elif escolha == "6":
        if usuario_logado:
            carrinho.ver_carrinho(usuario_logado)
        else:
            print("Faça o login primeiro.")
    elif escolha == "7":
        if usuario_logado:
            livros.apagar_livro()
        else:
            print("Faça o login primeiro.")
    elif escolha == "8":
        break
    else:
        print("Escolha inválida. Tente novamente.")