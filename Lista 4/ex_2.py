'''2 – Crie um programa que registrará as notas de um estudante. O programa deve
perguntar ao usuário quantas notas devem ser digitadas e, em seguida, fazer a leitura das
notas e, ao final, exibir todas as notas digitadas na tela'''

posicao = 0
notas = [] # lista vazia
notas_digitadas = int(input("Quantas notas deseja digitar? "))

while posicao < notas_digitadas:
    nota = float(input("Digite a nota:"))
    notas.append(nota) # adiciona a nota na lista
    posicao = posicao + 1   
print("As notas digitadas foram:")
for exibir in notas:
    print(exibir)