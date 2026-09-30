total_caixa = 0
cod =  int(input("Digite o código do produto: (de 1 á 8)"))
quant = int(input("Digite a quantidade desse produto que foi comprada:"))

if cod == 1:
    produto = "suco"
    valor = 6
    valor = valor * quant
    print(f"Você comprou {quant} suco(s) e custou R${valor}.")
elif cod == 2:
    valor = 3
    valor = valor * quant
    print(f"Você comprou {quant} pão(es) e custou R${valor}.")
elif cod == 3:
    valor = 7
    valor = valor * quant
    print(f"Você comprou {quant} pastel(is) e custou R${valor}.")
elif cod == 4:
    valor = 9
    valor = valor * quant
    print(f"Você comprou {quant} salada de fruta(s) e custou R${valor}.")
elif cod == 5:
    valor = 3.50
    valor = valor * quant
    print(f"Você comprou {quant} café(s) com leite e custou R${valor}.")
elif cod == 6:
    valor = 4.50
    valor = valor * quant
    print(f"Você comprou {quant} cappuccino(s) e custou R${valor}.")
elif cod == 7:
    valor = 6.50
    valor = valor * quant
    print(f"Você comprou {quant} iorgute(s) e custou R${valor}.")
elif cod == 8:
    valor = 2.50
    valor = valor * quant
    print(f"Você comprou {quant} água(s) e custou R${valor}.")