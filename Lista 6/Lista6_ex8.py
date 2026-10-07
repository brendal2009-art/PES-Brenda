'''– Implemente um algoritmo com as duas classes definidas logo abaixo. Seu algoritmo
deve ter um menu com as seguintes opções:

Sistema de Cadastro
-------------------
1 – Cadastrar estudante
2 – Cadastrar professor
3 – Listar estudantes
4 – Listar professores
5 – Alterar estudante pela matrícula
6 – Alterar estudante pelo nome
7 – Alterar professor pela matrícula
8 – Alterar professor pelo nome
9 – Excluir estudante pela matrícula
10 – Excluir professor pela matrícula
0 – Sair
'''

class Estudante:
    def __init__(self, nome, sobrenome, idade, matricula):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.matricula = matricula

class Professor:
    def __init__(self, nome, sobrenome, idade, matricula, especializacao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.matricula = matricula
        self.especializacao = especializacao

estudantes = [] # lista para armazenar os objetos Estudante
professores = [] # lista para armazenar os objetos Professor

while True:
    print("\nSistema de Cadastro", 
    "\n-------------------", 
    "\n1 – Cadastrar estudante", 
    "\n2 – Cadastrar professor",
    "\n3 – Listar estudantes",
    "\n4 – Listar professores",
    "\n5 – Alterar estudante pela matrícula",
    "\n6 – Alterar estudante pelo nome",
    "\n7 – Alterar professor pela matrícula",
    "\n8 – Alterar professor pelo nome",
    "\n9 – Excluir estudante pela matrícula",
    "\n10 – Excluir professor pela matrícula",
    "\n0 – Sair")
    
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome do estudante:")
        sobrenome = input("Digite o sobrenome do estudante:")
        idade = int(input("Digite a idade do estudante:"))
        matricula = input("Digite a matrícula do estudante:")

        estudante = Estudante(nome, sobrenome, idade, matricula)
        estudantes.append(estudante)

    elif opcao == 2:
        nome = input("Digite o nome do professor:")
        sobrenome = input("Digite o sobrenome do professor:")
        idade = int(input("Digite a idade do professor:"))
        matricula = input("Digite a matrícula do professor:")
        especializacao = input("Digite a especialização do professor:")

        professor = Professor(nome, sobrenome, idade, matricula, especializacao)
        professores.append(professor)

    elif opcao == 3:
        print("\nLista de Estudantes:")
        for estudante in estudantes:
            print(f"Nome: {estudante.nome} {estudante.sobrenome}, Idade: {estudante.idade}, Matrícula: {estudante.matricula}")

    elif opcao == 4:
        print("\nLista de Professores:")
        for professor in professores:
            print(f"Nome: {professor.nome} {professor.sobrenome}, Idade: {professor.idade}, Matrícula: {professor.matricula}, Especialização: {professor.especializacao}")

    elif opcao == 5:
        matricula = input("Digite a matrícula do estudante que deseja alterar:")
        for estudante in estudantes: 
            if estudante.matricula == matricula: # se a matrícula do estudante for igual a matrícula digitada, altere os dados do estudante
                estudante.nome = input("Digite o novo nome do estudante:")
                estudante.sobrenome = input("Digite o novo sobrenome do estudante:")
                estudante.idade = int(input("Digite a nova idade do estudante:"))
                print("Estudante alterado com sucesso!")
                break
        else:
            print("Estudante não encontrado.")

    elif opcao == 6:
        nome = input("Digite o nome do estudante que você deseja alterar: ")
        for estudante in estudantes:
            if estudante.nome == nome: # se o nome do estudante digitado for igual ao nome do estudante, altere os dados do estudante
                estudante.sobrenome = input("Digite o novo sobrenome do estudante:")
                estudante.idade = int(input("Digite a nova idade do estudante:"))
                estudante.matricula = input("Digite a nova matrícula do estudante:")
                print("Estudante alterado com sucesso!")
                break
        else:
            print("Estudante não encontrado.")

    elif opcao == 7:
        matricula = input("Digite a matrícula do professor que deseja alterar:")
        for professor in professores:
            if professor.matricula == matricula:
                professor.nome = input("Digite o novo nome do professor:")
                professor.sobrenome = input("Digite o novo sobrenome do professor:")
                professor.idade = int(input("Digite a nova idade do professor:"))
                professor.especializacao = input("Digite a nova especialização do professor:")
                print("Professor alterado com sucesso!")
                break
        else:
            print("Professor não encontrado.")

    elif opcao == 8:
        nome = input("Digite o nome do professor que deseja alterar: ")
        for professor in professores:
            if professor.nome == nome:
                professor.sobrenome = input("Digite o novo sobrenome do professor:")
                professor.idade = int(input("Digite a nova idade do professor:"))
                professor.matricula = input("Digite a nova matrícula do professor:")
                professor.especializacao = input("Digite a nova especialização do professor:")
                print("Professor alterado com sucesso!")
                break
        else:
            print("Professor não encontrado.")

    elif opcao == 9:
        matricula = input("Digite a matrícula do estudante que você deseja excluir: ")
        for estudante in estudantes:
            if estudante.matricula == matricula:
                estudantes.remove(estudante)
                print("Estudante excluído com sucesso!")
                break
        else:
            print("Estudante não encontrado.")

    elif opcao == 10:
        matricula = input("Digite a matrícula do professor que você deseja excluir: ")
        for professor in professores:
            if professor.matricula == matricula:
                professores.remove(professor) # remove o professor da lista de professores
                print("Professor excluído com sucesso!")
                break
        else:
            print("Professor não encontrado.")
    
    elif opcao == 0:
        print("Saindo do sistema...")
        break
    else: 
        print("Opção inválida. Tente novamente.")