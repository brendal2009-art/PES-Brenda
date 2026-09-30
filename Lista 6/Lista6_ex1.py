'''Crie uma classe chamda Livro com:
• Atributos titulo e autor.
• Um método chamado descricao que retorna: "{titulo} foi escrito por {autor}."
Teste criando um objeto e chamando o método para exibir a descrição.'''

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descricao(self):
        return f"{self.titulo} foi escrito por {self.autor}."

livro = Livro ("Harry Potter e a Pedra Filosofal" , "J.K. Rowling")
print(livro.descricao())