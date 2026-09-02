'''Faça um algoritmo que leia o preço de um produto e a quantidade comprada. Calcule o total
da compra e, caso ele seja maior ou igual a R$ 100,00, aplique um desconto de 10%. Ao final,
exiba o valor a ser pago.'''

preco = float(input("Digite o preço do produto: R$ "))
quantidade = int(input("Digite a quantidade comprada: "))

total = preco * quantidade

if total >= 100:
    total =  total - (total * 0.1)
    print("Parabéns!! você ganhou um cupom de 10% de desconto por sua compra chegar a R$100, agora o valor total da sua compra é de: R$ ", total)