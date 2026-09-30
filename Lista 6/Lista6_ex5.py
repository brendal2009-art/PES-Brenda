'''Crie uma classe chamada Pessoa com:
• Atributos: nome, idade, altura e peso;
• Um método para exibir, em uma única linha, o nome, a idade, a altura e o peso da
pessoa;
• Um método para retornar o IMC (Índice de Massa Corpórea) calculado da pessoa;
• Um método para retornar apenas o nome e o IMC da pessoa (em uma única linha).
Teste criando 3 pessoas com diferentes atributos e verificando se os IMCs calculados
estão corretos.'''

class Pessoa:
    def __init__ (self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def exibir(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}, Peso: {self.peso}')

    def imc(self):
        return self.peso / (self.altura ** 2) # ** altura ao quadrado -> exemplo: 1.75 ** 2 = 3.0625
    
    def nome_imc(self):
        return f'Nome: {self.nome}, IMC: {self.imc():.2f}' # :.2f -> mostra o resultado com 2 casas decimais, exemplo: 22,856879068 - > 22.86
    
pessoa1 = Pessoa("João", 23, 1.85, 75)
pessoa2 = Pessoa("Brenda", 17, 1.54, 53)
pessoa3 = Pessoa("Bruna", 16, 1.67, 68)

pessoa1.exibir()
pessoa2.exibir()
pessoa3.exibir()

print()

print(pessoa1.nome_imc())
print(pessoa2.nome_imc())
print(pessoa3.nome_imc())