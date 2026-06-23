'''2 – Crie um programa que leia 4 notas de um(a) determinado(a) estudante. Após a leitura
de todas notas, exiba a média aritmética simples e a situação final (aprovado(a) ou
reprovado(a)).'''

nota = [0]*4

nota[0] = float(input("Informe a primeira nota do estudante:"))
nota[1] = float(input("Informe a segunda nota do estudante:"))
nota[2] = float(input("Informe a terceira nota do estudante:"))
nota[3] = float(input("Informe a quarto nota do estudante:"))

soma = 0

for nums in nota:
    soma += nums
    media = soma / 4

print('A média do estudandte foi: ',media,' então ele está...')
      
if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')