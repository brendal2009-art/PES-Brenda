num = int(input("Digite um número"))

cont = 0

print(f"Tabuada do número {num}") # o "F" permite colocar varias variaveis, usando chaves {} para dizer onde a variavel é colocada, ex: o num = 9 ent aparecerá: "Tabuada do número 9"
while cont < 10: # enuqanto o cont for menor q 10 em vai pulando de 1 em 1, resumindo, de 0 a 9.
    cont = cont + 1 
    print(f"{num} x {cont} = {num * cont}") #"F" mostra a tabuada, ficará assim: se num informado = 9, fica: "9 x 1 = 9", "9 x 2 = 18", isso até "9 x 10 = 90".