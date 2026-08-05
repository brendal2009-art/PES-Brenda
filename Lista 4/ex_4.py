'''4 – Faça um algoritmo que solicite ao usuário a quantidade de cidades que devem ser
cadastradas em uma lista. Em seguida, faça a leitura das cidades e imprima o resultado
na tela. Ao final, solicite ao usuário o nome de uma cidade para ser removida, faça a
remoção dela e imprima a lista novamente.'''

posicao = 0
cidades = [] # cidades seria a lista das cidades informadas.
quantidade = int(input("Digite a quantidade de cidades que serão cadastradas: "))

while posicao < quantidade:
    cidade_informada = input("Digite o nome da cidade:")
    if cidade_informada in cidades: # verifica se a cidade já foi cadastrada
        print("Cidade já cadastrada, digite outra cidade.")
    else:
        cidades.append(cidade_informada) # adiciona a cidade na lista
        posicao += 1

quantidade = len(cidades) # le o tamanho da lista de cidades cadastradas
posicao = 0

while posicao < quantidade:
    print("cidades:", cidades[posicao]) # exibe a cidade cadastrada
    posicao += 1

print("Remova uma das cidades listadas.")
excluir = input("Digite o nome da cidade que deseja remover: ")

if excluir in cidades:
    print("Cidade removida com sucesso.")
    cidades.remove(excluir) # remove a cidade da lista
else:
    print("Cidade não encontrada na lista.")

    # lendo novamente dps da exclusão ->

quantidade = len(cidades) # le o tamanho da lista de cidades cadastradas
posicao= 0
print('\nAs cidades listadas são: ')

while posicao < quantidade:
 print(cidades[posicao]) # exibe a cidade cadastrada 
 posicao = posicao + 1