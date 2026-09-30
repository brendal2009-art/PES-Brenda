'''Crie uma classe chamada ContaBancaria com:
• Atributos: titular e saldo.
• Um método chamado depositar que recebe um valor e adiciona ao saldo.
• Um método chamado sacar que recebe um valor e subtrai do saldo (não precisa
validar o saldo).
• Um método chamado mostrar_saldo que retorna o saldo atual.
Teste criando uma conta, fazendo depósitos, saques e exibindo o saldo.'''

class ContaBancaria:

    def __init__(self,titular, saldo): 
        self.titular = titular # serve para armazenar o nome do titular da conta
        self.saldo = saldo # serve para armazenar o saldo da conta

    def depositar(self, valor):
        self.saldo = self.saldo + valor # serve para adicionar o valor depositado ao saldo da conta

    def sacar (self, valor):
        self.saldo =  self.saldo - valor # subtrai o valor sacado do saldo da conta

    def mostrar_saldo(self):
        return self.saldo # serve para retornar o saldo atual da conta
    
conta = ContaBancaria("João", 1000) # cria uma conta com o titular "João" e saldo inicial de 1000

conta.depositar(500) # deposita 500 na conta
conta.depositar(200) # deposita 200 na conta

conta.sacar(300) # saca 300 da conta

print("Titular:", conta.titular) # conta. titular retorna o nome do titular da conta
print("Saldo atual:", conta.mostrar_saldo()) # conta.mostrar_saldo() retorna o saldo atual da conta