def adicionar_contato(contatos, nome, telefone, email):
    #contato: nome, telefone, email, favorito
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print("\nContato adicionado com sucesso!")
    return

def ver_contatos(contatos):
    if not contatos:
        print("\nNenhum contato cadastrado.")
        return
    print("\nLista de Contatos:")
    for idx, contato in enumerate(contatos, start=1):
        favorito = "⭐" if contato["favorito"] else ""
        print(f"\n{idx}. {contato['nome']} - {contato['telefone']} - {contato['email']} {favorito}")
    return

def editar_contato(contatos, indice, novo_nome, novo_telefone, novo_email):
    if 0 <= indice < len(contatos):
        contatos[indice]["nome"] = novo_nome
        contatos[indice]["telefone"] = novo_telefone
        contatos[indice]["email"] = novo_email
        print("\nContato atualizado com sucesso!")
    else:
        print("\nÍndice inválido. Contato não encontrado.")
    return

def marcar_favorito(contatos, indice):
    if 0 <= indice < len(contatos):
        contatos[indice]["favorito"] = not contatos[indice]["favorito"]
        status = "favorito" if contatos[indice]["favorito"] else "não favorito"
        print(f"\nContato marcado como {status}!")
    else:
        print("\nÍndice inválido. Contato não encontrado.")
    return

def deletar_contato(contatos, indice):
    if 0 <= indice < len(contatos):
        contato_removido = contatos.pop(indice)
        print(f"\nContato '{contato_removido['nome']}' deletado com sucesso!")
    else:
        print("\nÍndice inválido. Contato não encontrado.")
    return


contatos = []
while True:
    print("\nMenu da Agenda de Contatos:")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar favorito")
    print("5. Deletar contato")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("\nDigite o nome do contato: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        adicionar_contato(contatos, nome, telefone, email)
    
    elif escolha == "2":
        ver_contatos(contatos)
    
    elif escolha == "3":
        ver_contatos(contatos)
        try:
            indice = int(input("\nDigite o número do contato a ser editado: ")) - 1
            novo_nome = input("Digite o novo nome: ")
            novo_telefone = input("Digite o novo telefone: ")
            novo_email = input("Digite o novo email: ")
            editar_contato(contatos, indice, novo_nome, novo_telefone, novo_email)
        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número válido.")
    elif escolha == "4":
        ver_contatos(contatos)
        try:
            indice = int(input("\nDigite o número do contato a ser marcado/desmarcado como favorito: ")) - 1
            marcar_favorito(contatos, indice)
        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número válido.")
    elif escolha == "5":
        ver_contatos(contatos)
        try:
            indice = int(input("\nDigite o número do contato a ser deletado: ")) - 1
            deletar_contato(contatos, indice)
        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número válido.")
    
    elif escolha == "6":
        print("\nSaindo da agenda de contatos. Até mais!")
        break
print("\nPrograma finalizado.")