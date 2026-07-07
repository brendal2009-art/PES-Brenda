''' 1 – Implemente um algoritmo com uma lista de nomes de bairros de Garopaba. O nome
do primeiro bairro deve ser adicionado manualmente (no próprio programa), em seguida,
deve ser solicitado ao usuário para cadastrar o nome de mais 5 bairros. Ao final, o
programa deve exibir o nome de todos os bairros cadastrados na tela.'''

posicao = 0
nome_bairros = ['Areia da palhocinha']

while posicao < 5:
    bairro = (input('Digite o nome do bairro: '))
    if bairro in nome_bairros:
        print("Bairro já cadastrado.")
    else:
        nome_bairros.append(bairro)
        posicao += 1

for exibir in nome_bairros:
    print("É um bairro de Garopaba: ",exibir) # exibir vai percorrer a lista e exibir cada elemento dela, nesse caso, cada bairro, mostrando o bairro para o usuário.