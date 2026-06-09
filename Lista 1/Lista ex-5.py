temperatura = float (input ("Informe  a temperatura de hoje em graus Celsius"))
if temperatura < 10:
    print ("Está muito frio! Use roupas quentes.")
elif temperatura >= 10 and temperatura <= 20:
    print ("Frio. Vista-se bem!")
elif temperatura > 20 and temperatura <= 25:
    print ("Temperatura agradável.")
elif temperatura > 25 and temperatura <= 30:
    print("Está ficando quente!")
else:
    print ("Está muito quente! Fique hidratado.")