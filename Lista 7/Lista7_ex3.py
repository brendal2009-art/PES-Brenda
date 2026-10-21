'''3 - VagaDeEstacionamento e Carro (0..1 - Associação Simples)

Objetivo: Modelar um relacionamento 0..1 onde a "parte" (Carro) vem de fora
(Agregação/Associação).

Classes: Carro e VagaDeEstacionamento.

Regras:
A classe Carro é simples, tem apenas placa e modelo.
    • A classe VagaDeEstacionamento tem um id_vaga (ex: "A-101").
    • Uma VagaDeEstacionamento pode estar ocupada por zero ou um Carro (0..1). O
    atributo carro_estacionado começa como None.
    • Crie um método ocupar_vaga(carro_obj). Este método deve verificar se a vaga já
    está None. Se estiver livre, associa o carro_obj (vindo de fora) à vaga e retorna
    True. Se já estiver ocupada, não faz nada e retorna False.
    • Crie um método liberar_vaga() que simplesmente seta carro_estacionado de volta
    para None.
Seu programa principal deve ter um menu interativo onde se possa testar todos os
métodos de um objeto do tipo VagaDeEstacionamento. Faça, também, o Diagrama de
Classes da sua implementação final.'''

class Carro:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo

    def __repr__(self):
        return f"Carro: {self.modelo} | Placa: {self.placa}"

class VagaDeEstacionamento:
    def __init__(self, id_vaga):
        self.id_vaga = id_vaga # Atributo que identifica a vaga de estacionamento
        self.carro_estacionado = None # Atributo que armazena o carro estacionado na vaga (inicialmente None)

    def ocupar_vaga(self, carro_obj):
        if self.carro_estacionado is None: # se a vaga estiver livre (carro_estacionado é None), associa o carro_obj à vaga
            self.carro_estacionado = carro_obj
            return True # retorna True indicando que a vaga foi ocupada com sucesso
        else:
            return False # retorna False indicando que a vaga já está ocupada

    def liberar_vaga(self):
        self.carro_estacionado = None # carro_estacionado é adicionado de volta para None, liberando a vaga

    def __repr__(self):
        if self.carro_estacionado: #  se carro_estacionado não for None, significa que a vaga está ocupada
            return f"Vaga {self.id_vaga} ocupada por {self.carro_estacionado}"
        else:
            return f"Vaga {self.id_vaga} livre"

# Programa principal com menu interativo

vaga = VagaDeEstacionamento("A-101") # Cria uma vaga de estacionamento com id "A-101"

while True:
    print("\nMenu:")
    print("1- Ocupar vaga")
    print("2- Liberar vaga")
    print("3- Consultar vaga")
    print("0- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        placa = input("Digite a placa do carro: ")
        modelo = input("Digite o modelo do carro: ")

        carro = Carro(placa, modelo) # Cria um objeto Carro com os dados fornecidos pelo usuário

        if vaga.ocupar_vaga(carro):
            print(f"Vaga {vaga.id_vaga} ocupada com sucesso!")
        else:
            print(f"Vaga {vaga.id_vaga} já está ocupada!")

    elif opcao == "2":
        vaga.liberar_vaga() # Libera a vaga
        print(f"Vaga {vaga.id_vaga} liberada!")

    elif opcao == "3":
        print(vaga) # Mostra o status da vaga (ocupada ou livre)

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Tente novamente.")