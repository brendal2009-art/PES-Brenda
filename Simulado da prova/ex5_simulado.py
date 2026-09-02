'''Desenvolva uma calculadora que leia dois números e apresente o seguinte menu:

• 1 – Adição;
• 2 – Subtração;
• 3 – Multiplicação;
• 4 – Divisão;
• 0 – Sair.

Realize a operação escolhida e exiba o resultado. Caso a opção seja inválida, apresente uma
mensagem de erro. O menu deve ser exibido novamente até que o usuário escolha a opção 0.'''

while True:
    print("\nMenu: " , "\n-----", "\n1 - Adição", "\n2 - Subtração", "\n3 - Multiplicação", "\n4 - Divisão", "\n0 - Sair")
    
    opcao = int(input("Digite a opção desejada: "))


    if opcao == 0:
        print("Encerrando o programa...")
        break

    elif opcao == 1:
        num1 = float(input("Digite o 1º número desejado: "))
        num2 = float(input("Digite o 2º número desejado: "))
    
        adicao = num1 + num2 
        print("Resultado: ", adicao)
        
    elif opcao == 2:
        num1 = float(input("Digite o 1º número desejado: "))
        num2 = float(input("Digite o 2º número desejado: "))
        
        subtracao = num1 - num2
        print("Resultado: ", subtracao)
        
    elif opcao == 3:
        num1 = float(input("Digite o 1º número desejado: "))
        num2 = float(input("Digite o 2º número desejado: "))
        
        multiplicacao = num1 * num2 
        print("Resultado: ", multiplicacao)
        
    elif opcao == 4:
        num1 = float(input("Digite o 1º número desejado: "))
        num2 = float(input("Digite o 2º número desejado: "))
        
        if num2 != 0:
            divisao = num1 / num2
            print("Resultado: ", divisao)  
        else:
            print("Não é possível dividir por 0!!") 
    else:
        print("Opção inválida!!")