menu = '''Menu
-----------
1- Adição
2- Subtração
3 – Divisão
4 – Multiplicação
0 - Sair
Digite a opção: ''' # pode de comentar sem ter q ser linha por linha

while True:
    print("\nMenu") #\n pula uma linha
    print("-----------")
    print("1- Adição")
    print("2- Subtração")
    print("3 – Divisão")
    print("4 – Multiplicação")
    print("0 - Sair")

    opção = input("Digite a opção")

    if opção ==  "0":
        print("Fechando programa...")
        break #se a opção for 0 fecha o programa e pausa o código

    if opção not in ["1", "2", "3", "4"]: # se a opção nao estiver no 1, 2 , 3 ou 4, a opção é inválida
        print("Opção inválida, escolha outra opção.")
        continue

    num1 = float(input("Digite o primeiro número:")) #float pq o número pode ser decimal
    num2 = float(input("Digite o segundo número"))

    if opção == "1":
        print("Resultado:", num1 + num2)
    elif opção == "2":
        print("Resultado:", num1 - num2)
    elif opção == "3":
        if num2 == 0:
            print("Divisão por 0 n é permitida!!!")
        else:
            print("Resultado:", num1 / num2)
    elif opção == "4":
        print("Resultado:", num1 * num2)