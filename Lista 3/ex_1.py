'''1 - Implemente um programa com um cadastro de idades de 6 alunos utilizando lista. O
programa deve solicitar as idades dos 6 alunos. Após informar todas as idades, deve-se
apresentar apenas as idades que forem maiores ou iguais a 16.'''

idade = [0]*6 # o tamanho da lista ta definida no num que esta multiplicando 

idade[0] = int(input("Informe a idade do primeiro aluno:"))
idade[1] = int(input("Informe a idade do segundo aluno:"))
idade[2] = int(input("Informe a idade do terceiro aluno:"))
idade[3] = int(input("Informe a idade do quarto aluno:"))
idade[4] = int(input("Informe a idade do quinto aluno:"))
idade[5] = int(input("Informe a idade do sexto aluno:"))
for num in idade: # para os numeros que estiverem dentro da idade... diga se sem maiores ou iguais a 16
    if num >= 16:
        print('As idades maiores ou iguais a 16 são: ', num)