'''3 – Utilizando como base o exercício anterior, faça com seu programa exiba uma saída
formatada da forma exibida abaixo (abaixo é utilizado com exemplo com 3 notas). Você
deve fazer isso de duas formas: com while e com for.

-QUADRO-

Exibição com while:
Nota: 9.0
Nota: 7.5
Nota: 8.0

Exibição com for:
Nota: 9.0
Nota: 7.5
Nota: 8.0'''

#Com while

'''posicao = 0
notas = []
quantidade = int(input('Quantas notas serão cadastradas? '))

while posicao < quantidade:
    nota_informada = float(input("Digite a primeira nota: "))
    notas.append(nota_informada)
    posicao += 1

for exibir in notas:
    print('Nota: ', exibir)'''

# com while

posicao = 0
notas = [] # notas seria a lista das notas informadas.
quantidade =  int(input('Quantas notas serão cadastradas? '))

while posicao < quantidade:
    nota_informada = float(input("Digite a nota: "))
    notas.append(nota_informada)
    posicao += 1

quantidade = len(notas) # len() retorna a quantidade de elementos da lista
posicao = 0
while posicao < quantidade:
    print('Nota: ', notas[posicao])
    posicao += 1