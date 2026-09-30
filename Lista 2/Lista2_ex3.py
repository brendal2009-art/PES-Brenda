num = int(input("Digite um número: "))

cont = 1 # contador começa em 1

if num >= 1: # se o número for maior ou igual a 1, o contador vai contar de 1 até o número digitado
    while cont <= num: # enquanto o contador for menor ou igual ao número
        print(cont)
        cont = cont + 1 # o contador vai aumentando de 1 em 1
else:
    while cont >= num: # se o número for menor que 1, o contador vai contar de 1 até o número digitado
        print(cont)
        cont = cont - 1 # o contador vai diminuindo de 1 em 1