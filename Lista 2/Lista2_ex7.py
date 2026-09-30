quant = int(input("Digite a quantidade de notas:"))

soma = 0
cont = 1

while cont <=  quant:
   nota = float(input("Digite a nota:")) # float pq a nota pode ser decimal: ex: "7,5"
   soma = soma + nota # soma das notas
   cont = cont + 1 # aumenta o contador de notas

media = soma / quant # calcula a media, usando a soma e dividando pela quantidade de notas informadas
print ("A média das notas é:", media)

if media >= 6: # se a media for maior ou igual que 6 é aprovado
  print ("Você foi aprovado!")

else:
   print ("Você foi reprovado!") # se nao for maior ou igual a 6 está reprovado