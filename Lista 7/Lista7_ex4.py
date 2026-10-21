'''4- Funcionario e ContratoDeTrabalho (1..1).

Objetivo: Modelar um 1..1 onde a "parte" (Contrato) é obrigatória e contém a lógica de
cálculo que o "todo" (Funcionario) utiliza.

Classes: ContratoDeTrabalho e Funcionario.

Regras:
    • A classe ContratoDeTrabalho deve ter salario_bruto (float) e percentual_impostos
    (float, ex: 0.11 para 11% de INSS).
    • O ContratoDeTrabalho deve ter um método chamado valor_impostos que calcula e
    retorna o valor exato do desconto (ex: salario_bruto * percentual_impostos).
    • A classe Funcionario deve ter nome e cargo.
    • Um Funcionario deve ter exatamente um ContratoDeTrabalho para ser criado
    (1..1).
    • O __init__ do Funcionario deve receber nome, cargo, e também o salario_bruto e o
    percentual_impostos necessários para criar sua própria instância de
    ContratoDeTrabalho (Composição). O atributo funcionario.contrato nunca pode ser
    None.
    • Crie um método chamado salario_liquido na classe Funcionario. Este método deve:
        ◦ Acessar o salario_bruto do seu contrato.
        ◦ Acessar o valor_impostos calculado pelo seu contrato.
        ◦ Retornar o salario_bruto menos o valor_impostos.

Seu programa principal deve ter um menu interativo onde se possa testar todos os
métodos de um objeto do tipo Funcionario. Faça, também, o Diagrama de Classes da sua
implementação final'''

class ContratoDeTrabalho:
    def __init__(self, salario_bruto, percentual_impostos):
        self.salario_bruto = salario_bruto
        self.percentual_impostos = percentual_impostos

    def valor_impostos(self):
        return self.salario_bruto * self.percentual_impostos

class Funcionario:
    def __init__(self, nome, cargo, salario_bruto, percentual_impostos):
        self.nome = nome
        self.cargo = cargo
        self.contrato = ContratoDeTrabalho(salario_bruto, percentual_impostos) 

    def salario_liquido(self):
        return self.contrato.salario_bruto - self.contrato.valor_impostos() # acessa o salario bruto e o valor dos impostos do contrato e retorna o valor do salario bruto menos o valor dos impostos pagos

    def __repr__(self):
        return f"Funcionario: {self.nome} | Cargo: {self.cargo}"

# Programa principal com menu interativo:

funcionario = Funcionario("Brenda", "Desenvolvedora", 3000.00, 0.11)

while True:
    print("\nMenu:")
    print("1- Consultar funcionário")
    print("2- Consultar salário bruto")
    print("3- Consultar valor dos impostos")
    print("4- Consultar salário líquido")
    print("0- Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print(funcionario)

    elif opcao == "2":
        print(f"Salário bruto: R$ {funcionario.contrato.salario_bruto:.2f}")

    elif opcao == "3":
        impostos = funcionario.contrato.valor_impostos()
        print(f"Valor dos impostos: R$ {impostos:.2f}")

    elif opcao == "4":
        print(f"Salário líquido: R$ {funcionario.salario_liquido():.2f}")

    elif opcao == "0":
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida!")