divida = 1000.0
juros = 15.3 / 100

meses = int(input("Digite a quantidade de meses: "))

contador = 1

while contador <= meses:
    divida = divida + (divida * juros)
    contador = contador + 1

print("Dívida após", meses, "meses: R$", divida)