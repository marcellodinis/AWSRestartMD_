
# Estruturas de controlo: if e match
while True: # Ciclo infinito
    print("""
        Menu:
        1 - Primavera
        2 - Verão
        3 - Outono
        4 - Inverno
        5 / 6 - humm...
        7 - Sair
    """)

    try:
        estacao_ano = int(input("Indique um número de 1 a 7:\n"))
    except:
        print("Erro: Deverá introduzir um valor inteiro!\n")
    else:

        match estacao_ano:
            case 1:
                print("Primavera")
            case 2:
                print("Verão")
            case 3:
                print("Outono")
            case 4:
                print("Inverno")
            case 5 | 6: # Opção 1 | ou Opção 2. o | é um "OR"
                print("nope.")
            case 7:
                print("Sair")
                break
            case _:
                print("Valor inválido")
