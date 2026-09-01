''' Elabore um algoritmo que leia 15 números de uma cartela de bingo e armazene-os em uma lista.
Aceite apenas números entre 1 e 75 e não permita valores repetidos. Ao final, ordene a lista e
exiba os números do menor para o maior.'''

cartela = []

while len(cartela) < 15: #enquanto a cartela tiver menos de 15 números, continue pedindo número
    numero = int(input(f"Digite o {len(cartela) + 1}º número de uma cartela de bingo (1 a 75): "))
    if numero < 1 or numero > 75:
        print("Número inválido! Digite um número entre 1 e 75.")
    elif numero in cartela:
        print("Número repetido! Digite outro número.")

    else:
        cartela.append(numero)
cartela.sort() #coloca os números em ordem crescente

print("Números da cartela de bingo em ordem crescente:", cartela)