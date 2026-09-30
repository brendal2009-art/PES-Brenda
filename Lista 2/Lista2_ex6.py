num = int(input("Digite o número da tabuada:"))
inicio = int(input("Digite o inicio da tabuada:"))
fim = int(input("Digite o fim da tabuada:"))

while inicio <= fim: # enquanto o inicio for menor ou igual ao fim
    print(f"{num} x {inicio} = {num * inicio}") # tabuada do num multiplicado pelo inicio
    inicio = inicio + 1 # aumenta o inicio de 1 em 1
