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


professores = { # { serve para quando queremos trabalhar com nome ou espaço específico
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
        while indice<len(prof):
            print(f'Código:{prof[indice]["cod"]} - {prof[indice]["nome"]}') #lista os professores ja cadastrados
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

        indice = 0

        while indice < len(acesso):

            print(f'{i + 1} - {acesso[i]["lab"]}')

            i += 1

        numero_lab = int(input("Escolha o laboratório: "))

        indice_lab = numero_lab - 1

        if indice_lab >= 0 and indice_lab < len(acesso):

            # Mostrar professores
            print("\nProfessores cadastrados:")

            i = 0

            while i < len(prof):

                print(
                    f'Código: {prof[i]["cod"]} - '
                    f'{prof[i]["nome"]}'
                )

                i += 1

            codigo_professor = input(
                "Digite o código do professor: "
            )

            # Procurar professor
            indice_prof = 0

            while indice_prof < len(prof):

                if prof[indice_prof]["cod"] == codigo_professor:
                    break

                indice_prof += 1

            if indice_prof < len(prof):

                nome_professor = prof[indice_prof]["nome"]

                # Verificar se já possui acesso
                if nome_professor in acesso[indice_lab]["profs"]:

                    print(
                        "Esse professor já possui acesso "
                        "a esse laboratório!"
                    )

                else:

                    acesso[indice_lab]["profs"].append(
                        nome_professor
                    )

                    print(
                        "Professor adicionado ao laboratório "
                        "com sucesso!"
                    )

            else:

                print("Professor não encontrado!")

        else:

            print("Laboratório inválido!")