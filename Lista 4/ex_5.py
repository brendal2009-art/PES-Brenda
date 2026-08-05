'''5 – Crie um programa que funcionará como um cadastro de Amigos Próximos no
Instagram. Seu programa deve permitir que amigos sejam cadastrados ou removidos,
conforme a solicitação do usuário. Também deve ser possível exibir a lista com todos os
amigos cadastrados, porém, o programa deve avisar o usuário caso a lista esteja vazia.
Crie um menu, conforme abaixo, para permitir a interação com o seu programa:

Menu:

Amigos Próximos
---------------
1 - Cadastrar
2 - Excluir
3 - Listar
0 - Sair'''

posicao = 0
amigos = [] # lista vazia

while True:
    print('\nMenu: ', '\nAmigos Próximos', '\n---------------', '\n1 - Cadastrar', '\n2 - Excluir', '\n3 - Listar', '\n0 - Sair')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        usuario = input('Digite o usuario do amigo que você deseja cadastrar: ')
        amigos.append(usuario) #amigos.append(usuario) adiciona o usuario na lista amigos
        print(f'O usuário {usuario} foi cadastrado com sucesso!')

    elif opcao == 2:
        if len(amigos) == 0:
            print(f'A lista de amigos próximos está vazia! Não é possível que você exclua nenhum amigo.')
        else:
            usuario = input('Digite o usuário do amigo próximo que você deseja excluir:')
            if usuario in amigos:
                amigos.remove(usuario) # amigos.remove(usuario) remove o usuario da lista amigos
                print(f'O usuário {usuario} foi excluido da sua lista de amigos próximos com sucesso!')

    elif opcao == 3:
        if len(amigos) == 0:
            print(f'A sua lista de amigos próximos está vazia! ')
        else:
            print('Lista de amigos próximos: ')
            for amigo in amigos: #para cada amigo na lista amigos, imprima o amigo
                print(amigo) #mostra o amigo na tela

    elif opcao == 0:
        print('Encerrando o programa...')
        break