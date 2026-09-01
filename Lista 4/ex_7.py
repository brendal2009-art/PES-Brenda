'''7 – Utilizando como base o exercício 6, implemente dois novos recursos: um para
informar a maior nota cadastrada e outro para informar a menor nota cadastrada. Caso
não existam notas cadastradas, seu programa deve informar “Erro: não há notas
cadastradas”. Crie um menu, conforme abaixo, para permitir a interação com o seu
programa:
Notas
-----
1 - Cadastrar
2 - Excluir
3 - Listar
4 - Calcular média
5 – Mostrar maior nota
6 – Mostrar menor nota
0 - Sair'''

notas = []

while True:
    print('\nNotas', '\n-----', '\n1 - Cadastrar', '\n2 - Excluir', '\n3 - Listar', '\n4 - Calcular média', '\n5 - Mostrar maior nota', '\n6 - Mostrar menor nota', '\n0 - Sair')
    opcao = int(input('Digite a opção desejada:'))
    
    if opcao == 1:
        nota = float(input('Digite a noota que deseja cadastrar:'))
        notas.append(nota) #adiciona a nota na lista de notas

    elif opcao == 2:
        if  len(notas) == 0:
            print('A lista de notas está vazia! você não pode excluir nenhuma nota. ')
        else:
            nota = float(input('Digite a nota que deseja excluir:'))
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

    elif opcao == 5:
        if len(notas) == 0:
            print('Erro: não há notas cadastradas')
        else:
            maior_nota = max(notas) #max retorna o maior valor da lista de notas
            print(f'A maior nota cadastrada é: {maior_nota}')

    elif opcao == 6:
        if len(notas) == 0:
            print('Erro: não há notas cadastradas')
        else:
            menor_nota = min(notas) #min retorna o menor valor da lista de notas
            print(f'A menor nota cadastrada é: {menor_nota}')

    elif opcao == 0:
        print('Encerrando o programa...')
        break