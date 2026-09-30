caminhoes = {
    "001": "Monobloco",
    "002": "Scania 112 HW",
    "003": "Volkswagen Express 4150",
    "004": "Volkswagen Express 6160",
    "005": "Volkswagen VW 17230 Worker",
    "006": "Volkswagen Express 9170",
    "007": "Iveco Daily 40s14",
    "008": "Iveco Tectro 310E28"
}

condutores = {
    "001": "Roberto Souza",
    "002": "João Graciano",
    "003": "Karine Silva",
    "004": "Pedro Luiz",
    "005": "Maria Catarina",
    "006": "Júlio Cardoso",
    "007": "Altivo Antônio",
    "008": "Jorge Gonçalves",
    "009": "Marcos Vinícius",
    "010": "Heleno Nunes",
    "011": "Mara Cristina",
    "012": "Otávio Rocha"
}

viagens = []

while True:

    print("""
    1 - Listar caminhões
    2 - Listar condutores
    3 - Registrar saída
    4 - Registrar retorno
    5 - Consultar caminhão
    6 - Listar retornos por data
    7 - Verificar entregas do dia
    8 - Listar caminhões em rota
    0 - Sair
""")
    
    opcao = input("Digite a opção desejada: ").strip()

    if opcao == "1":
        print("\nCADASTRO DOS CAMINHÕES:")

        for codigo, modelo in caminhoes.items():
            print(f"{codigo} - {modelo}")

    elif opcao == "2":
        print("\nCADASTRO DOS CONDUTORES:")

        for codigo, nome in condutores.items():
            print(f"{codigo} - {nome}")


    elif opcao == "3":
        print("\nREGISTRO DE SAÍDA:")
        cod_caminhao = input("Código do caminhão: ").strip()

        if cod_caminhao not in caminhoes:
            print("Caminhão não cadastrado!")
            continue

        # Um caminhão que possui uma viagem sem retorno ainda está em rota.
        if any(
            viagem["caminhao"] == cod_caminhao
            and viagem["retorno"] is None
            for viagem in viagens
        ):
            print("Este caminhão já está em rota!")
            continue

        cod_condutor = input("Código do condutor: ").strip()

        if cod_condutor not in condutores:
            print("Condutor não cadastrado!")
            continue

        if any(
            viagem["condutor"] == cod_condutor
            and viagem["retorno"] is None
            for viagem in viagens
        ):
            print("Este condutor já está em rota!")
            continue

        data_saida = input("Data da saída (DD/MM/AAAA): ").strip()
        destino = input("Destino da viagem: ").strip()

        viagens.append({
            "caminhao": cod_caminhao,
            "condutor": cod_condutor,
            "saida": data_saida,
            "destino": destino,
            "retorno": None,
        })

        print("Saída registrada com sucesso!")
        print(f"Caminhão: {caminhoes[cod_caminhao]}")
        print(f"Condutor: {condutores[cod_condutor]}")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")
