'''6 – Elabore um programa que funcionará como um cadastro notas de um estudante. Seu
programa deve permitir que notas sejam cadastradas ou removidas (através do seu
índice, pois podem haver notas repetidas), conforme a solicitação do usuário. Também
deve ser possível exibir a lista com todas as notas cadastradas, porém, o programa deve
avisar o usuário caso a lista esteja vazia. O programa também deve ter uma opção para
calcular a média do aluno e exibir sua situação (aprovado se média for maior ou igual a 6
e reprovado, caso contrário). Crie um menu, conforme abaixo, para permitir a interação
com o seu programa:
Notas
-----
1 - Cadastrar
2 - Excluir
3 - Listar
4 - Calcular média
0 - Sair'''

notas = [] #diz que a lista de notas está vazia

while True:
    print('\nNotas', '\n-----', '\n1 - Cadastrar', '\n2 - Excluir', '\n3 - Listar', '\n4 - Calcular média', '\n0 - Sair')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        nota = float(input('Digite a nota que você deseja cadastrar: '))
        notas.append(nota) # adiciona a nota na lista de notas

    elif opcao == 2:
        if len(notas) == 0:
            print ('A lista de notas está vazia! você não pode excluir nenhuma nota. ')
        else:
            nota = float(input('Digte a nota que você deseja excluir: '))
        if nota in notas:
            notas.remove(nota) #remove a nota da lista de notas
            print('Nota excluida com sucesso!')

    elif opcao == 3:
            if len(notas) == 0:
                print('A lista de notas está vazia! ')
            else:
                print('As notas cadastradas são:')
                for nota in notas: #para cada nota na lista de notas, imprima a nota
                    print(nota) #mostra a nota na tela

    elif opcao == 4:
            if len(notas) == 0:
                print('A lista de notas está vazia. ')
            else:
                soma = 0

                for nota in notas:
                    soma = soma + nota #soma todas as notas da lista de notas

                media = soma / len(notas) #calcula a média das notas
                print(f'A média do estudante é: {media:.2f}') #.2f transforma a média para 2 casas decimais.

                if media >= 6:
                    print('O estudante está aprovado! ')
                else:
                    print('O estudante está reprovado! ')

    elif opcao == 0:
            print('Encerrando o programa... ')
            break