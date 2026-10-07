'''Utilizando como base a classe Pessoa do exercício anterior, crie um algoritmo que
funcionará como um cadastro de pessoas em uma lista. Seu algoritmo deve ter um menu
conforme abaixo:

Cadastro de Pessoas
-------------------
1 – Cadastrar
2 – Listar
0 – Sair
Opção: '''

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
pessoas = [] # lista para armazenar os objetos Pessoa

while True:
    print("\nCadastro de Pessoas", 
    "\n-------------------", 
    "\n1 – Cadastrar", 
    "\n2 – Listar", 
    "\n0 – Sair")
   
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        cpf = input("Digite o CPF: ")

        pessoa = Pessoa(nome, idade, cpf) # mostrando que a pessoa cadastrada é um objeto da classe Pessoa
        pessoas.append(pessoa) # adiciona o objeto pessoa na lista pessoas

        print(f"Pessoa cadastrada: {pessoa.nome}, {pessoa.idade} anos, CPF: {pessoa.cpf}") # apresenta os dados da pessoa cadastrada

    elif opcao == 2:
        print("Listando pessoas cadastradas...")
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
            for pessoa in pessoas:
                print(f"Nome: {pessoa.nome} - Idade: {pessoa.idade} - CPF: {pessoa.cpf}") #pessoa.nome serve para acessar o atributo nome do objeto pessoa.

    elif opcao == 0:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!!")