def addContact(contacts, contactName, contactPhoneNumber, contactEmail):
    contact = {"contactName":contactName, "contactPhoneNumber":contactPhoneNumber, "contactEmail":contactEmail, "favorite":False}
    contacts.append(contact)
    print(f"Contato '{contactName}' foi adicionado com sucesso!")
    return

def viewContacts(contacts):
    print("CONTATOS:")
    for index, contact in enumerate(contacts, start=1):
        status = "☆" if contact["favorite"] else " "
        contactName = contact["contactName"]
        print(f"{index} | [ {status} ] - {contactName} | {contactPhoneNumber} | {contactEmail}")
    return

def updateContact(contacts, indexContact, updateNameContact,updateContactPhoneNumber, updateContactEmail):
    indexContactAdjusted = int(indexContact) - 1
    if indexContactAdjusted >= 0 and indexContactAdjusted < len(contacts):
        contacts[indexContactAdjusted]["contactName"] = updateNameContact
        contacts[indexContactAdjusted]["contactPhoneNumber"] = updateContactPhoneNumber
        contacts[indexContactAdjusted]["contactEmail"] = updateContactEmail
        print(f"Contato {indexContact} foi atualizado para {updateNameContact} com sucesso!")
        print(f"Número do contato {indexContact} foi atualizado para {updateContactPhoneNumber} com sucesso!")
        print(f"Email do contato {indexContact} foi atualizado para {updateContactEmail} com sucesso!")
    else:
        print("Opção inválida!")
    return

def favorite(contacts, indexContact):
    indexContactAdjusted = int(indexContact) - 1
    if contacts[indexContactAdjusted]["favorite"]:
        contacts[indexContactAdjusted]["favorite"] = False
    else:
        contacts[indexContactAdjusted]["favorite"] = True
    print(f"Contato {indexContact} foi marcado/desmarcado como favorito com sucesso!")
    return

def viewFavoritesContacts(contacts):
    print("CONTATOS FAVORITOS:")
    for index, contact in enumerate(contacts, start=1):
        status = "☆" if contact["favorite"] else " "
        contactName = contact["contactName"]
        if contact["favorite"]:
            print(f"{index} | [ {status} ] - {contactName} | {contactPhoneNumber} | {contactEmail}")
    return

def deleteContact(contacts, indexContact):
    indexContactAdjusted = int(indexContact) - 1
    for index, contact in enumerate(contacts):
        if indexContactAdjusted == index:
            contacts.remove(contact)
            print(f"Contato {indexContact} deletado com sucesso.")
    return

contacts = []

while True:
    print("\n######################################")
    print("######    LISTA DE CONTATOS:    ######")
    print("######################################\n")
    print("1 | ADICIONAR UM CONTATO.")
    print("2 | VISUALIZAR CONTATOS.")
    print("3 | EDITAR UM CONTATO.")
    print("4 | MARCAR/DESMARCAR COMO FAVORITO.")
    print("5 | EXIBIR CONTATOS FAVORITOS.")
    print("6 | DELETAR UM CONTATO.")
    print("7 | ENCERRAR A APLICAÇÃO.\n")
    print("######################################\n")

    option = input("Selecione o número da opção desejada: ")

    if option == '1':
        contactName = input("Insira o nome do contato: ")
        contactPhoneNumber = input("Insira o número de telefone do contato: ")
        contactEmail = input("Insira o E-mail do contato: ")
        addContact(contacts, contactName, contactPhoneNumber, contactEmail)
    
    elif option == '2':
        viewContacts(contacts)

    elif option == '3':
        viewContacts(contacts)
        indexContact = input("Qual contato deseja alterar? ")
        updateNameContact = input("Qual o novo nome para o contato? ")
        updateContactPhoneNumber = input("Insira o novo número de telefone: ")
        updateContactEmail = input("Insira o novo E-mail do contato: ")
        updateContact(contacts, indexContact, updateNameContact,contactPhoneNumber, contactEmail)

    elif option == '4':
        viewContacts(contacts)
        indexContact = input("Qual contato deseja marcar/desmarcar como favorito? ")
        favorite(contacts, indexContact)
    
    elif option == '5':
        viewFavoritesContacts(contacts)

    elif option == '6':
        viewContacts(contacts)
        indexContact = input("Qual contato deseja deletar? ")
        deleteContact(contacts, indexContact)

    elif option == '7':
        break

print("APLICAÇÃO ENCERRADA!")

