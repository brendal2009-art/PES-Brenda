'''6 – Adicione ao programa da questão anterior, uma opção para excluir o cadastro
baseado no código da pessoa. Adicione também uma opção para pesquisar que utilizará
o nome da pessoa como critério de busca.

Questão anterior:


5 – Faça um programa que funcionará como um cadastro de medidas corpóreas. Seu
programa deve ter uma estrutura que seja capaz de armazenar as seguintes informações
sobre cada pessoa: nome, idade, altura e peso (cada uma em uma lista). A interação deve
ser através de um menu com as seguintes opções:
Menu
-----
1 – Cadastrar
2 - Excluir
3 - Alterar
4 - Listar
0 - Sair
A opção Cadastrar deve solicitar as informações da pessoa a ser cadastrada. Já a opção
excluir, deve solicitar o nome de quem se deseja excluir o cadastro. A opção Alterar deve
solicitar o nome da pessoa a ser alterado e, em seguida, solicitar as novas informações
da pessoa (idade, altura e peso). A opção Listar deve apresentar todas as informações
das pessoas cadastradas.'''

codigo = [0] * 20
nome = [0] * 20
idade = [0] * 20
altura = [0] * 20
peso = [0] * 20

while True:
    print('\nMenu', '\n-----', '\n1 - Cadastrar', '\n2 - Excluir por codigo', '\n3 - Alterar', '\n4 - Listar', '\n5 - Pesquisar por nome', '\n0 - Sair')

    opcao = int(input("Digite uma opcao: "))

    if opcao == 1:
        if 0 in nome: # ve se tem espaço na lista de nomes (se tem alguma posição com valor 0, indica que não há cadastro naquela posição)
            posicao = nome.index(0) # pega a posição do primeiro elemento com valor 0 na lista de nomes, que indica que não há cadastro naquela posição
            codigo_informado = int(input("Codigo: ")) #mostra a mensagem código para o usuario digitar o valor

            if codigo_informado in codigo: # se o código informado já estiver na lista de códigos, significa que o código já foi cadastrado
                print("Codigo ja cadastrado.")
            else:
                nome_informado = input("Nome: ")
                idade_informada = int(input("Idade: "))
                peso_informado = float(input("Peso: "))
                altura_informada = float(input("Altura: "))

                codigo[posicao] = codigo_informado # atribui o valor do código informado pelo usuário na posição encontrada na lista de códigos
                nome[posicao] = nome_informado # atribui o valor do nome informado pelo usuário na posição encontrada na lista de nomes
                idade[posicao] = idade_informada # atribui o valor da idade informada pelo usuário na posição encontrada na lista de idades
                altura[posicao] = altura_informada # atribui o valor da altura informada pelo usuário na posição encontrada na lista de alturas
                peso[posicao] = peso_informado # atribui o valor do peso informado pelo usuário na posição encontrada na lista de pesos
                print("Cadastro realizado com sucesso.")
        else:
            print("Nao ha espaco disponivel.")

    elif opcao == 2:
        codigo_informado = int(input("Digite o codigo que deseja excluir: "))

        if codigo_informado in codigo: # se o código informado estiver na lista de códigos, significa que o cadastro existe e pode ser excluído
            posicao = codigo.index(codigo_informado) # pega a posição do código informado na lista de códigos
            codigo[posicao] = 0 # atribui o valor 0 na posição encontrada na lista de códigos, indicando que o cadastro foi excluído
            nome[posicao] = 0 
            idade[posicao] = 0
            altura[posicao] = 0
            peso[posicao] = 0
            print("Cadastro excluido com sucesso.")
        else:
            print("Codigo nao encontrado.")

    elif opcao == 3:
        nome_informado = input("Digite o nome que deseja alterar: ")

        if nome_informado in nome: # se o nome informado estiver na lista de nomes, significa que o cadastro existe e pode ser alterado
            posicao = nome.index(nome_informado) # pega a posição do nome informado na lista de nomes
            idade[posicao] = int(input("Nova idade: "))
            altura[posicao] = float(input("Nova altura: "))
            peso[posicao] = float(input("Novo peso: "))
            print("Cadastro alterado com sucesso.")
        else:
            print("Nome nao encontrado.")

    elif opcao == 4:
        print("\nCadastros:")

        for i in range(20): # percorre todas as posições das listas de cadastro (de 0 a 19)
            if nome[i] != 0:
                print(f"Codigo: {codigo[i]}, Nome: {nome[i]}, Idade: {idade[i]}, Altura: {altura[i]}, Peso: {peso[i]}") # imprime as informações do cadastro na posição i, caso o nome não seja 0 (ou seja, caso haja um cadastro naquela posição)

    elif opcao == 5:
        nome_informado = input("Digite o nome que deseja pesquisar: ")

        if nome_informado in nome:
            posicao = nome.index(nome_informado) # pega a posição do nome informado na lista de nomes
            print(f"Codigo: {codigo[posicao]}, Nome: {nome[posicao]}, Idade: {idade[posicao]}, Altura: {altura[posicao]}, Peso: {peso[posicao]}") # imprime as informações do cadastro na posição i, caso o nome informado esteja na lista de nomes
        else:
            print("Nome nao encontrado.")

    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opcao invalida.")
