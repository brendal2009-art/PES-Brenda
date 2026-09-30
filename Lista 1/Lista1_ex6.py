jogador1 = input ("Vamos jogar pedra, papel ou tesoura, digite oque você quer jogar. pedra, papel ou tesoura?")
jogador2 = input("Vamos jogar pedra, papel ou tesoura, digite oque você quer jogar. pedra, papel ou tesoura?")
if jogador1 == jogador2:
    print ("Empate!!")
elif ((jogador1 == "pedra" and jogador2 == "tesoura") or (jogador1 == "tesoura" and jogador2 == "papel") or (jogador1 == "papel" and jogador2 == "pedra")):
    print ("Jogador 1 venceu!!")
else:
    print ("Jogador 2 venceu!!")