''' Crie um dicionário de palavras da língua portuguesa, utilizando as palavras como chaves e seus
significados como valores. Inicie com:

"apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma
situação difícil, ou usar de meios extremos e exagerados"

Solicite ao usuário mais 4 palavras e seus respectivos significados. Em seguida, peça uma
palavra para consulta e exiba seu significado. Caso ela não esteja cadastrada, informe “Palavra
não encontrada”.'''

dicionario = {
    "apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma situação difícil, ou usar de meios extremos e exagerados"
}

for i in range(4):
    palavra = input(f"Digite a {i + 1}ª palavra: ") #f serve para formatar a string, colocando o valor de i + 1 no lugar do {}
    significado = input(f"Digite o significado da {i + 1}ª palavra: ")
    dicionario[palavra] = significado
    
consulta = input("Digite a palavra que você deseja consultar: ")

if consulta in dicionario: # se a palavra digitada pelo usuário estiver no dicionário, o programa entra no if
    print("`Significado: ", dicionario[consulta]) #dicionario[consulta] retorna o valor que esta na chave consulta no dicionário. Exemplo: se a palavra for "apelar", o valor retornado será "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma situação difícil, ou usar de meios extremos e exagerados"
else:
    print("Palavra não encontrada!!")