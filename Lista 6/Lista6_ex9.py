'''Utilizando a biblioteca pickle, implemente duas novas opções para salvar e carregar
dados do disco, utilizando como base, o exercício 7.'''

import pickle

class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    
pessoas = [] # lista para armazenar os objetos Pessoa

while True:
    print("\nCadastro de Pessoas", 
    "\n-------------------", 
    "\n1 – Cadastrar", 
    "\n2 – Listar",
    "\n3 – Excluir pelo nome",
    "\n4 – Atualizar idade altura e peso pelo nome",
    "\n5 – Salvar dados",
    "\n6 – Carregar dados",
    "\n0 – Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        altura = input("Digite sua altura: ")
        peso = input("Digite seu peso: ")

        pessoa = Pessoa(nome, idade, altura, peso) # mostrando que a pessoa cadastrada é um objeto da classe Pessoa
        pessoas.append(pessoa) # adiciona o objeto pessoa na lista pessoas

        print(f"Pessoa cadastrada: {pessoa.nome}, {pessoa.idade} anos, {pessoa.altura} cm, {pessoa.peso} kg") # apresenta os dados da pessoa cadastrada

    elif opcao == 2:
        print("Listando pessoas cadastradas...")
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
            for pessoa in pessoas:
                print(f"Nome: {pessoa.nome} - Idade: {pessoa.idade} - Altura: {pessoa.altura} - Peso: {pessoa.peso} kg") #pessoa.nome serve para acessar o atributo nome do objeto pessoa.

    elif opcao == 3:
        excluir = input("Digite o nome da pessoa que deseja excluir: ")
        for pessoa in pessoas:
            if pessoa.nome == excluir: # se o nome da pessoa for igual ao nome informado, então exclui a pessoa
                pessoas.remove(pessoa)
                print(f"Pessoa {excluir} excluída com sucesso!")

    elif opcao == 4:
        atualizar = input("Digite o nome da pessoa que deseja atualizar: ")
        for pessoa in pessoas:
            if pessoa.nome == atualizar: # se o nome da pessoa for igual ao nome informado, então atualiza os dados
                nova_idade = int(input("Digite a nova idade: "))
                nova_altura = input("Digite a nova altura: ")
                novo_peso = input("Digite o novo peso: ")
                pessoa.idade = nova_idade # atualiza a idade da pessoa
                pessoa.altura = nova_altura
                pessoa.peso = novo_peso
                print(f"{atualizar} foi atualizada(o) com sucesso!")

    elif opcao == 5:
        with open("pessoas.pkl", "wb") as arquivo: # abre o arquivo pessoas.pkl, wb significa write binary = escrever em binário, pessoas.pkl é o nome do arquivo que será criado para salvar os dados
            pickle.dump(pessoas, arquivo) # dump é oq salva dados no aqquivo, pessoas é a lista de objetos que vai ser salva no arquivo, arquivo é o nome do arquivo que vai ser salvo

        print("Dados salvos com sucesso!")

    elif opcao == 6:
        with open("pessoas.pkl", "rb") as arquivo: # abre o arquivo pessoas.pkl, rb significa read binary = ler em binário, pessoas.pkl é o nome do arquivo que será aberto para carregar os dados
            pessoas = pickle.load(arquivo) # load é oq carrega os dados do arquivo, pessoas é a lista de objetos que vai ser carregada do arquivo, arquivo é o nome do arquivo que vai ser carregado

        print("Dados carregados com sucesso!")

    elif opcao == 0:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!!")