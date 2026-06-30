'''3 – Faça um programa que funcionará como um cadastro de códigos de produtos de uma
loja de roupas. O cadastro deve ser realizado em uma lista com até 10 códigos. Inicialize
os elementos da lista com -1, este valor indicará que o elemento está vago para o
cadastro. Seu programa deve ter um menu com uma opção para cadastrar um novo
código (apenas um por vez) e para listar os todos códigos cadastrados (não devem ser
listados códigos não cadastrados). Deve-se também informar se houve sucesso ou falha
na hora de cadastrar um novo código e também não deve ser possível cadastrar um
produto com o código -1. No momento do cadastro, não deve ser informado o valor do
índice, esse deve ser “calculado” automaticamente. Veja como deve ser criado o menu:
Menu
----
1 – Cadastrar
2 – Listar todos
0 – Sair '''

codigos = [-1] * 10

posicao = 0

while True:
    print('\nMenu', '\n----', '\n1 – Cadastrar', '\n2 – Listar todos', '\n0 – Sair')
    opcao = int(input("Digite uma opção:"))

    if opcao == 1: #se a opcao for a 1(Cadastrar)
        if posicao < 10: #se a posição for menor q dez
            codigo = int(input("Digite o código do produto"))
            if codigo != - 1: # se o código nao for -1, ent codigo aceito
                codigos[posicao] = codigo # "guarde o valor digitado (codigo) na posição posicao da lista codigos."
                posicao =  posicao + 1 #contador aumenta mais 1 
                print("Código cadastrado com sucesso")
            else:
                print("Código inválido")
        else:
            print("Não há mais esoaço para armazenar seus códigos.")
    elif opcao == 2:
        print('\n Códigos cadastrados:')
        for codigo in codigos:
            if codigo != -1:
                print(codigo)
    elif opcao == 0:
        print("Fechando seu programa...")
        break

    else:
        print("Opção inválida")