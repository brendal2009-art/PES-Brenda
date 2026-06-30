'''4 - Codifique um programa que funcionará como um cadastro de placas de automóveis de
um estacionamento (para até 15 automóveis). O cadastro deve ser realizado em uma
lista. Seu programa deve ter um menu com a seguinte estrutura:
Menu
----
1 – Cadastrar
2 - Excluir
3 - Listar
0 - Sair'''

placas = [0] * 15

while True:
    print('\nMenu', '\n----', '\n1 – Cadastrar', '\n2 - Excluir',' \n3 - Listar', '\n0 - Sair')

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        if 0 in placas: #se tiver espaço livre, digite a placa do automóvel.
            placa = input("Digite a placa do automóvel: ")

            posicao = placas.index(0) # coloca a placa dentro da primeira vaga livre da lista, 0 para representar uma vaga vazia.
            placas[posicao] = placa # Substitui o 0 pela placa digitada pelo usuário.
            print("Placa cadastrada com sucesso.")
        else:
            print("Não há espaço disponível.")

    elif opcao == 2:
        placa = input("Digite a placa que deseja excluir: ")

        if placa in placas: # a placa que o usuário digitou existe dentro da lista placas?
            posicao = placas.index(placa) # qual posição da lista está essa placa.
            placas[posicao] = 0 # Essa linha troca a placa por 0, apaga a placa e deixa a vaga livre de novo.
            print("Placa excluída com sucesso.")
        else:
            print("Placa não encontrada.")

    elif opcao == 3:
        print("\nPlacas cadastradas:")

        for placa in placas: # a placa que o usuário digitou existe dentro da lista placas?
            if placa != 0: # se a placa nao for 0 (0= vaga vazia)
                print(placa) # mostra a placa na tela

    elif opcao == 0:
        print("Fechando o programa...")
        break

    else:
        print("Opção inválida.")
