lista_contatos = []

def adicionarContato():
    contato = {
        "nome": input("Digite o nome: "),
        "telefone": int(input("Digite o telefone: "))
    }
    
    lista_contatos.append(contato)

def removerContato():
    remover = input("Digite o nome do contato a ser removido: ")
    
    for elemento in lista_contatos:
        if elemento["nome"] == remover:
            lista_contatos.remove(elemento)
            print("Contato removido!")
            break
    else:
        print("Este contato não existe em sua agenda")

def buscarContato():
    busca = input("Digite o nome do contato a ser encontrado: ")
    
    for elemento in lista_contatos:
        if elemento["nome"] == busca:
            print(f"Nome: {elemento['nome']}, Telefone: {elemento['telefone']}")
            break
        else:
            print("Este contato não existe na sua agenda")

def listarContatos():
    if lista_contatos:
        for contato in lista_contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")
    else:
        print("A lista de contatos está vazia")

while True:

    opcao = int(input("Selicione uma das opções a seguir: \n 1- Adicionar contato \n 2- Remover contato \n 3- Buscar contato \n 4- Listar contatos \n"))

    if opcao == 1:
        adicionarContato()
    elif opcao == 2:
        removerContato()
    elif opcao == 3:
        buscarContato()
    elif opcao == 4:
        listarContatos()
    else:
        print("Escolha uma das opções listadas a cima!")

