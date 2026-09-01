'''Desenvolva um algoritmo que leia um ano e informe se ele é bissexto. Um ano é bissexto quando
é divisível por 400 ou quando é divisível por 4, mas não é divisível por 100.'''

ano = int(input("Digite um ano:"))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")