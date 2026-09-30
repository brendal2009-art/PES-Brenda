idade = int (input("Informe sua idade"))
if idade < 10:
    print ("Você pode assistir apenas a filmes com classificação Livre.")
elif idade == 10 or idade == 11:
    print ("Você pode assistir a filmes com classificação até 10 anos.")
elif idade == 12 or idade == 13:
    print ("Você pode assistir a filmes com classificação até 12 anos.")
elif idade == 14 or idade == 15:
    print ("Você pode assistir a filmes com classificação até 14 anos.")
elif idade == 16 or idade == 17:
    print ("Você pode assistir a filmes com classificação até 16 anos.")
else:
    print ("Você pode assistir a filmes com classificação até 18 anos.")