meses = int(input("Você esta devendo a quantos meses? "))

if meses >= 24:
    print("O tempo quitou a dívida pra você")
else:
    porcentagem = (1000*15.3)/100
    valor = porcentagem*meses
    print(f"Você esta devendo R${valor} ao banco.")