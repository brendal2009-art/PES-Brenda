'''1 - Nossa necessidade é utilizar o recurso de liberação de portas dos Laboratórios de
Informática utilizando os dispositivos instalados em cada porta com fechadura eletrônica.
Para tal, desenvolveremos um sistema que identifique e autorize a entrada dos
professores já cadastrados no sistema de uso dos laboratórios.
O sistema deve possuir:


• Um cadastro completo de professores (adicionar, alterar, excluir e listar) que
associe o código do professor ao seu nome, alguns professores já devem ser précadastrados, veja a lista abaixo;


• Um cadastro completo dos acessos dos professores aos laboratórios (adicionar,
alterar, excluir e listar), serão utilizados 6 laboratórios com as nomenclaturas
Lab102, Lab103, Lab104, Lab105, Lab106, Lab107 – os laboratórios são fixos no
sistema, o que pode ser alterado são os acessos, alguns professores já devem
ser pré-cadastrados nos laboratórios, veja a outra lista abaixo (para facilitar a
implementação, sugere-se que os laboratórios sejam associados ao código do
professor e não ao seu nome);


• Teste de acesso ao laboratório: deve ser possível informar o nome de um
laboratório e um código de professor para verificar se o acesso é permitido ou não
(por exemplo, nesse teste deveria ser possível escolher o Lab103 e informar o
código de professor 002, nesse caso, o sistema deve negar o acesso).


Pré-cadastro de Professores (códigos x nomes)

001 – Prof Thiago Paes
002 – Prof Schalata
003 – Prof Ignácio
004 – Prof Ryan
005 – Prof André
006 – Profª Fabiana
007 – Prof Alberto
008 – Prof Juliano
009 – Prof Thiago Waltrik
010 – Prof João Eduardo

Pré-cadastro de Acessos (laboratório x professor)

• Lab102 – Prof Ignácio, Prof Thiago Paes, Profª Ryan, Prof André, Profª Fabiana;

• Lab103 – Prof Alberto;

• Lab104 – Prof Ryan, Prof Juliano, Prof Schalata, Prof André;

• Lab105 – Prof Ignácio, Prof Alberto, Prof Thiago Waltrik, Prof Thiago Paes;

• Lab106 – Prof Schalata, Prof Ignácio, Prof Thiago Waltrik, Prof Thiago Paes;

• Lab107 – Prof André, Prof Schalata, Prof Thiago Waltrik, Prof Thiago Paes, Prof João Eduardo.'''


professor = { # { serve para quando queremos trabalhar com nome ou espaço específico
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

laboratorios = {
    "Lab102",
    "Lab103",
    "Lab104",
    "Lab105",
    "Lab106",
    "Lab107"
}

acesso = {
    "Lab102": ["003", "001", "004", "005", "006"],
    "Lab103": ["007"],
    "Lab104": ["004", "008", "002", "005"],
    "Lab105": ["003", "007", "009", "001"],
    "Lab106": ["002", "003", "009", "001"],
    "Lab107": ["005", "002", "009", "001", "010"]
}

   

opcao = -1

while opcao != 0:
    print ("""Menu:
        ----
        1 – Cadastrar professor;
        2 - Excluir professor;
        3 - Alterar professor;
        4 - Listar professores;
        5 - Labs: Adicionar professor
        6 - Labs: Excluir professor
        7 - Labs: Alterar professor
        8 - Listar laboratórios
        0 - Sair""")
    
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        cod = int("Digite o código do professor:")
        nome = int(input("Digite o nome do professor;"))
        professor.append({
            "nome": nome, 
            "cod": cod,
        })

    elif opcao == 2:
        print("Excluir")
        
        indice = 0
        while indice<len(professor):
            print(f'Código:{professor[indice]["cod"]} - {professor[indice]["nome"]}') #lista os professores ja cadastrados
            indice = indice + 1 
        
        excluir = input("Quem você deseja excluir? (informe o código) ")
        
        indice = 0

        while indice < len(professor):
            if professor[indice]["cod"] == excluir:
                break
            indice= indice + 1

        professor.pop(indice) #pop remove um elemento da lista usando o índice.

        print("Professor deletado com sucesso!")

    elif opcao == 3:
        print("Alterar")

        indice = 0

        while indice<len(professor):
            print(f'Código:{professor[indice]["cod"]} - {professor[indice]["nome"]}')
            indice+=1
        alterar = input("Informe o código do professor que você deseja alterar:")
        
        indice = 0

        while indice < len(professor):
            if professor[indice]["cod"] == alterar:
                break
            indice+=1

        professor[indice]["cod"]=(input("Qual o novo código?  "))
        professor[indice]["nome"]=(input("Qual o novo nome?  "))

    elif opcao == 4:
        print("Listar")

        if len(professor) == 0:
            print("A lista está vazia, cadastre algum professor.")
        else:
            indice = 0
            while indice<len(professor):
                print(f'Código:{professor[indice]["cod"]} - {professor[indice]["nome"]}')
                indice+=1

    elif opcao == 5:
        print("Adicionar professor ao laboratório")

        print("Laboratórios disponíveis:")
        for lab in laboratorios: #mostra os laboratorios que estao disponiveis
            print(lab)

        lab = input("Informe o laboratório: ")

        if lab in laboratorios:
            print("Professores cadastrados:") 

            for cod, nome in professor.items():
                print(f"Código: {cod} - {nome}") #mostra o codigo e o nome dos professores cadastrados

            cod = input("Informe o código do professor: ")

            if cod in professor:  
                if cod in acesso[lab]: #se o cod ja estiver acesso no lab...
                    print("Este professor já possui acesso a este laboratório!")
                else:
                    acesso[lab].append(cod) #se ele nao estiver acesso ainda, o cod é adicionado ao laboratorio
                    print("Professor adicionado ao laboratório com sucesso!")
            else:
                print("Professor não encontrado!")
        else:
            print("Laboratório inválido!")

    elif opcao == 6:
        print("Excluir professor do laboratório")

        print("Laboratórios disponíveis:")
        for lab in laboratorios:
            print(lab) #mostra os labs disponíveis

        lab = input("Informe o laboratório: ") 

        if lab in laboratorios:
            print(f"Professores com acesso ao {lab}:") #"profesores com acesso ao lab 107"

            for cod in acesso[lab]:
                print(f"Código: {cod} - {professor[cod]}") #mostra os professores que tem acesso ao laboratorio selecionado

            cod = input("Informe o código do professor que deseja excluir: ")

            if cod in acesso[lab]:
                acesso[lab].remove(cod) #remove o codigo que tem acesso ao lab da lista de códigos dos professores que tem acesso ao laboratorio
                print("Professor excluído do laboratório com sucesso!")
            else:
                print("Este professor não possui acesso a este laboratório!")
        else:
            print("Laboratório inválido!")

    elif opcao == 7:
        print("Alterar professor do laboratório")

        print("Laboratórios disponíveis:")
        for lab in laboratorios:
            print(lab) #motra os labs disponíveis

        lab = input("Informe o laboratório: ")

        if lab in laboratorios:
            print(f"Professores com acesso ao {lab}:") #"profesores com acesso ao lab 107"

            for cod in acesso[lab]:
                print(f"Código: {cod} - {professor[cod]}") #mostra os professores que tem acesso ao laboratorio selecionado

            alterado = input("Informe o código do professor que deseja alterar: ")

            if alterado in acesso[lab]: # passa pela lista de acessos do lab
                novo_cod = input("Informe o novo código do professor: ")

                if novo_cod in professor:
                    if novo_cod in acesso[lab]: # se o cod novo ja estiver na lista de acessos...
                        print("Este professor já possui acesso a este laboratório!")
                    else:
                        indice = acesso[lab].index(alterado) #index descobre a posição de um elemento dentro de uma lista.
                        acesso[lab][indice] = novo_cod 
                        print("Acesso alterado com sucesso!")
                else:
                    print("Professor não encontrado!")

            else:
                print("Este professor não possui acesso a este laboratório!")

        else:
            print("Laboratório inválido!")


    elif opcao == 8:
        print("Listar laboratórios")

        for lab in laboratorios:
            print(f"\n{lab}")

            if len(acesso[lab]) == 0:
                print("Nenhum professor possui acesso.")
            else:
                for cod in acesso[lab]:
                    print(f"Código: {cod} - {professores[cod]}")


    elif opcao == 0
        print("Encerrando programa...")
    break