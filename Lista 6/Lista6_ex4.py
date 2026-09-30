'''Crie uma classe chamada Produto com:
• Atributos: nome e quantidade.
• Um método chamado esta_disponivel que retorna True se a quantidade for maior
que 0 e False caso contrário.
• Um método chamado vender que diminui a quantidade em 1.
Teste criando um objeto, verificando a disponibilidade, vendendo produtos e verificando
novamente.'''

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def esta_disponivel(self):
        return self.quantidade > 0
    
    def vender(self):
        if self.quantidade > 0:  # se a quantidade for maior que 0, diminui a quantidade em 1
            self.quantidade = self.quantidade - 1

produto = Produto("Caderno", 3)

print(produto.nome) # Caderno
print("Disponível:", produto.esta_disponivel()) # pruduto.esta_disponivel() retorna True, pq a qtd é 3

produto.vender() # vendendo 1 produto
print("Quantidade após a venda:", produto.quantidade) # mostra a quantidade atualizada, que é 2
print("Disponível?", produto.esta_disponivel()) # pruduto.esta_disponivel() retorna True, pq a qtd é 2

produto.vender() 
print("Quantidade após a venda:", produto.quantidade) # mostra a quantidade atualizada, que é 1
print("Disponível?", produto.esta_disponivel()) # pruduto.esta_disponivel() retorna True, pq a qtd é 1

produto.vender()
print("Quantidade após tentar vender:", produto.quantidade) # mostra a quantidade atualizada, que é 0
print("Disponível?", produto.esta_disponivel()) # pruduto.esta_disponivel() retorna False, pq a qtd é 0