professor = {
    "001": "Prof Thiago Paes",
    "002": "Prof Schalata",
    "003": "Prof Ignácio",
    "004": "Prof Ryan",
    "005": "Prof André",
    "006": "Profª Fabiana",
    "007": "Prof Alberto",
    "008": "Prof Juliano",
    "009": "Prof Thiago Waltrik",
    "010": "Prof João Eduardo"
}

laboratorios = [
    "Lab102",
    "Lab103",
    "Lab104",
    "Lab105",
    "Lab106",
    "Lab107"
]

acesso = {  # Cada laboratório possui uma lista com os códigos dos professores que possuem acesso
    "Lab102": ["003", "001", "004", "005", "006"],
    "Lab103": ["007"],
    "Lab104": ["004", "008", "002", "005"],
    "Lab105": ["003", "007", "009", "001"],
    "Lab106": ["002", "003", "009", "001"],
    "Lab107": ["005", "002", "009", "001", "010"]
}

while True:

    print("""
        -MENU-
--------------------------
1 - Cadastrar professor
2 - Excluir professor
3 - Alterar professor
4 - Listar professores
5 - Adicionar professor ao laboratório
6 - Excluir professor do laboratório
7 - Alterar acesso ao laboratório
8 - Listar laboratórios e acessos
9 - Testar acesso ao laboratório
0 - Sair
""")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("\n-CADASTRAR PROFESSOR-")
        
        cod = input("Digite o código do professor: ")

        if cod in professor: # se o cod desejado jà estiver na lista de professor...
            print("Erro: este código já está cadastrado!")

        else:
            nome = input("Digite o nome do professor: ")

            professor[cod] = nome #Coloca no dicionário "professor" o valor "nome", usando "cod" como chave. Ex: professor["011"] = "Prof Camila"
            print("Professor cadastrado com sucesso!")

    elif opcao == "2":

        print("\n-EXCLUIR PROFESSOR-")
        if len(professor) == 0: #len conta quantos elementos tem na lista de professor, se tiver 0 então nenhum pode ser excluído
            print("Não existem professores cadastrados.")

        else:
            for cod, nome in professor.items(): #o ".items()" percorre a chave e valor do dicionário. Ex: priemira volta-> cod = "001" nome = "Prof Thiago Paes"; segunda volta-> cod = "002" nome = "Prof Schalata"

                print(f"Código: {cod} - {nome}") #código: 001 - Prof Thiago Paes

            cod = input("\nDigite o código do professor que deseja excluir: ")

            if cod in professor:

                for lab in laboratorios: 
                    if cod in acesso[lab]:
                        acesso[lab].remove(cod) #antes de excluir o professor, removemos seus acessos aos laboratórios.

                del professor[cod] #del exclui do dicionário professor o valor que está armazenada na variável cod. Ex: "003": "Prof Ignácio"
                print("Professor excluído com sucesso!")

            else:
                print("Professor não encontrado!")

    elif opcao == "3":

        print("\n-ALTERAR PROFESSOR-")

        for cod, nome in professor.items():
            print(f"Código: {cod} - {nome}")

        cod = input("\nDigite o código do professor que deseja alterar: ")

        if cod in professor: # se o cod estive no dicionario professor...

            novo_cod = input("Digite o novo código: ")

            if novo_cod != cod and novo_cod in professor: # O novo código é diferente do código atual? O novo código já pertence a outro professor?

                print("Erro: o novo código já está cadastrado!")

            else:

                novo_nome = input("Digite o novo nome: ")

                if novo_cod != cod: # Se o código mudou...

                    for lab in laboratorios: #Percorre os laboratórios.

                        if cod in acesso[lab]: #Procura o código antigo nos acessos.

                            indice = acesso[lab].index(cod) #.index() encontra a posição daquele código.
                            acesso[lab][indice] = novo_cod #Substitui o código antigo pelo novo.

                    professor[novo_cod] = novo_nome #Cria o professor usando o novo código.
                    del professor[cod] #Apaga o código antigo.

                else:
                    professor[cod] = novo_nome #Se o usuário não mudou o código, muda o nome.
                print("Professor alterado com sucesso!")

        else:
            print("Professor não encontrado!")

    elif opcao == "4":

        print("\n-PROFESSORES CADASTRADOS-")

        if len(professor) == 0:
            print("Nenhum professor cadastrado.")

        else:

            for cod, nome in professor.items():
                print(f"Código: {cod} - {nome}")

    elif opcao == "5":

        print("\n-ADICIONAR ACESSO AO LABORATÓRIO-")

        print("\nLaboratórios disponíveis:")

        for lab in laboratorios: #percorre a lista de laboratórios e mostra os labs disponíveis
            print(lab)

        lab = input("\nDigite o laboratório desejado: ")

        if lab not in laboratorios: #se o lab digitado não estiver na lista de laboratórios disponíveis...
            print("Laboratório inválido!")

        else:
            print("\nProfessores cadastrados:")

            for cod, nome in professor.items():
                print(f"Código: {cod} - {nome}")

            cod = input("\nDigite o código do professor: ")

            if cod not in professor: #se o codigo digitado não estiver na lista de professor...
                print("Professor não encontrado!")

            elif cod in acesso[lab]: #se o cod ja tiver acesso ao lab...
                print("Este professor já possui acesso a este laboratório!")

            else:
                acesso[lab].append(cod) #adiciona o cod a lista de acesso dos labs
                print("Acesso adicionado com sucesso!")

    elif opcao == "6":

        print("\n-EXCLUIR ACESSO AO LABORATÓRIO -")

        print("\nLaboratórios disponíveis:")

        for lab in laboratorios:
            print(lab)

        lab = input("\nDigite o laboratório: ")

        if lab not in laboratorios: # se o lab digitado nao estiver na lista de laborátorios disponíveis...
            print("Laboratório inválido!")

        else:
            print(f"\nProfessores com acesso ao {lab}:") #mostra os professores com acesso ao lab digitado

            if len(acesso[lab]) == 0:
                print("Nenhum professor possui acesso.")

            else:
                for cod in acesso[lab]:
                    print(f"Código: {cod} - {professor[cod]}")

                cod = input("\nDigite o código do professor que deseja excluir: ")

                if cod in acesso[lab]:
                    acesso[lab].remove(cod)
                    print("Acesso excluído com sucesso!")

                else:
                    print("Este professor não possui acesso a este laboratório!")

    elif opcao == "7":

        print("\n-ALTERAR ACESSO AO LABORATÓRIO-")

        print("\nLaboratórios disponíveis:")
        for lab in laboratorios:
            print(lab)

        lab = input("\nDigite o laboratório: ")

        if lab not in laboratorios:
            print("Laboratório inválido!")

        else:
            print(f"\nProfessores com acesso ao {lab}:")

            if len(acesso[lab]) == 0:
                print("Nenhum professor possui acesso.")

            else:
                for cod in acesso[lab]:
                    print(f"Código: {cod} - {professor[cod]}")

                antigo_cod = input("\nDigite o código do professor que deseja alterar: ")

                if antigo_cod not in acesso[lab]:
                    print("Este professor não possui acesso a este laboratório!")

                else:
                    novo_cod = input("Digite o novo código do professor: ")

                    if novo_cod not in professor:
                        print("Professor não encontrado!")

                    elif novo_cod in acesso[lab]:
                        print("Este professor já possui acesso a este laboratório!")

                    else:
                        indice = acesso[lab].index(antigo_cod) #Descobre onde o código antigo está na lista.
                        acesso[lab][indice] = novo_cod #Substitui o código antigo pelo novo.
                        print("Acesso alterado com sucesso!")

    elif opcao == "8":

        print("\n-LABORATÓRIOS E ACESSOS-")

        for lab in laboratorios:
            print(f"\n{lab}")

            if len(acesso[lab]) == 0:
                print("  Nenhum professor possui acesso.")

            else:
                for cod in acesso[lab]:
                    print(f"Código: {cod} - {professor[cod]}")

    elif opcao == "9":

        print("\n-TESTE DE ACESSO-")

        print("\nLaboratórios disponíveis:")

        for lab in laboratorios:
            print(lab)

        lab = input("\nDigite o laboratório: ")

        if lab not in laboratorios:
            print("Laboratório inválido!")

        else:
            cod = input("Digite o código do professor: ")

            if cod not in professor:
                print("Professor não encontrado!")

            elif cod in acesso[lab]:
                print("\nACESSO PERMITIDO!")

                print(f"{professor[cod]} possui acesso ao {lab}.")

            else:
                print("\nACESSO NEGADO!")

                print(f"{professor[cod]} NÃO possui acesso ao {lab}.")

    elif opcao == "0":
        print("\nEncerrando programa...")
        break

    else:

        print("\nOpção inválida! Digite uma opção de 0 a 9.")