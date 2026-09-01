'''5 – Faça um programa que funcionará como um cadastro de medidas corpóreas. Seu
programa deve ter uma estrutura que seja capaz de armazenar as seguintes informações
sobre cada pessoa: nome, idade, altura e peso (cada uma em uma lista). A interação deve
ser através de um menu com as seguintes opções:
Menu
-----
1 – Cadastrar
2 - Excluir
3 - Alterar
4 - Listar
0 - Sair
A opção Cadastrar deve solicitar as informações da pessoa a ser cadastrada. Já a opção
excluir, deve solicitar o nome de quem se deseja excluir o cadastro. A opção Alterar deve
solicitar o nome da pessoa a ser alterado e, em seguida, solicitar as novas informações
da pessoa (idade, altura e peso). A opção Listar deve apresentar todas as informações
das pessoas cadastradas.'''

nome =[0] * 20
idade = [0] * 20
altura =[0] * 20
peso =[0] * 20

while True:
    print('\nMenu', '\n-----', '\n1 - Cadastrar', '\n2 - Excluir', '\n3 - Alterar', '\n4 - Listar', '\n0 - Sair')

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        if 0 in nome: # se tiver espaço livre, digite o nome da pessoa.
            posicao = nome.index(0) # coloca o nome dentro da primeira vaga livre da lista, 0 para representar uma vaga vazia.
            nome_informado = input("Nome:")

            if nome_informado in nome:
                print("Nome já cadastrado.")
            else:
                idade_informada = int(input("Idade:"))
                peso_informado = float(input("Peso:"))
                altura_informada = float(input("Altura:"))

                nome[posicao] = nome_informado
                idade[posicao] = idade_informada
                altura[posicao] = altura_informada
                peso[posicao] = peso_informado
                print("Cadastro realizado com sucesso.")
        else:
            print("Não há espaço disponível.")

    elif opcao == 2:
        nome_informado = input("Digite o nome que deseja excluir: ")

        if nome_informado in nome: # o nome que o usuário digitou existe dentro da lista nome?
            posicao = nome.index(nome_informado) # qual posição da lista está esse nome.
            nome[posicao] = 0 # troca o nome por 0, apaga o nome e deixa a vaga livre de novo.
            idade[posicao] = 0
            altura[posicao] = 0
            peso[posicao] = 0
            print("Cadastro excluído com sucesso.")
        else:
            print("Nome não encontrado.")

    elif opcao == 3:
        nome_informado = input("Digite o nome que deseja alterar: ")

        if nome_informado in nome:
            posicao = nome.index(nome_informado) # qual posição da lista está esse nome.
            idade[posicao] = int(input("Nova idade:"))
            altura[posicao] = float(input("Nova altura:"))
            peso[posicao] = float(input("Novo peso:"))
            print("Cadastro alterado com sucesso.")
        else:
            print("Nome não encontrado.")

    elif opcao == 4:
        print("\nCadastros:")

        for i in range(20):
            if nome[i] != 0: # se o nome nao for 0 (0 = vaga vazia)
                print(f"Nome: {nome[i]}, Idade: {idade[i]}, Altura: {altura[i]}, Peso: {peso[i]}")

    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")