'''1 - Livro e MarcadorDePagina (0..1).
Objetivo: Implementar um relacionamento opcional simples.
Classes: MarcadorDePagina e Livro.
Regras:
• A classe MarcadorDePagina deve ter um atributo pagina_atual.
• A classe Livro deve ter um atributo titulo e um total_paginas.
• Um Livro pode ter zero ou um MarcadorDePagina (ele começa sem marcador,
0..1).
• Crie um método no Livro chamado adicionar_marcador(pagina). Este método deve
criar uma instância de MarcadorDePagina e associá-la ao livro. Se o livro já tiver
um marcador, apenas atualize a pagina_atual dele.
Comprove o funcionamento da sua implementação no programa principal.
Veja, na figura abaixo, o Diagrama de Classes completo:

MarcadorDePagina
+ pagina_atual

+ __init__(pagina_atual)
+ __repr__(): str

Livro
+ titulo
+ total_paginas

+ __init__(titulo, total_paginas)
+ __repr__(): str
+ adicionar_marcador(pagina)'''

class MarcadorDePagina:
    def __init__(self, pagina_atual):
        self.pagina_atual = pagina_atual

    def __repr__(self): # repr serve para mostrar a representação do objeto, ou seja, o que será exibido quando chamarmos o objeto no print
        return f"Marcador de Pagina {self.pagina_atual}" # programa vai substitui "{self.paginaatual}" pelo número da página onde o usuário parou.

class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.marcador = None # none significa que o livro começa sem marcador, ou seja, 0..1, self.marcador armazena a instância de MarcadorDePagina, se tiver

    def __repr__(self):
        return f"Livro: {self.titulo}" # livro vai mostrar o título do livro quando chamarmos o objeto no print

    def adicionar_marcador(self, pagina):
        if self.marcador is None: # se o livro não tiver marcador, cria uma instância de MarcadorDePagina e associa ao livro
            self.marcador = MarcadorDePagina(pagina)
        else:
            self.marcador.pagina_atual = pagina # se o livro já tiver marcador, apenas atualiza a pagina_atual dele

# Programa principal

livro1 = Livro("Harry Potter e a Pedra Filosofal", 223)

print(livro1) # vai mostrar o título do livro
print("Marcador inicial:", livro1.marcador) # vai mostrar None, pois o livro começa sem marcador

livro1.adicionar_marcador(30) # adiciona marcador na página 30
print("Marcador após adicionar:", livro1.marcador) # vai mostrar o marcador com a página atual 100

livro1.adicionar_marcador(80) # atualiza marcador para a página 80
print("Marcador após atualizar:", livro1.marcador) # vai mostrar o marcador com a página atual 120