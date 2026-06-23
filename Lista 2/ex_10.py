n = int(input("Digite um número inteiro:"))
soma = n #inicia a variável soma com o primeiro número digitado
cont = 1 #Como o primeiro número já foi digitado, o contador começa em 1.
while n != 0: #O programa continuará pedindo números enquanto n for diferente de 0.
    n = int(input("Digite outro numero inteiro: "))
    cont = cont + 1 #ada número digitado é contado.
    soma = soma + n #Adiciona o novo número à soma acumulada.

cont -= 1 # tira o valor atribuido e adiciona um novo valor, número 0 foi contado pelo comando: mas ele não deve ser considerado como um número válido da sequência.

media = soma / cont
print("0 é o único número proibido.​")
print(f"Você inseriu {cont} números, a soma deles é = {soma} e a média é = {media}")