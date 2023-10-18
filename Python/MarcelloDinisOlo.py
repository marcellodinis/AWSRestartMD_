#Mensagem de boas vindas ao utilizar.

print("**************** Sistema de reservas Hotel Notas Musicais ★★★★★ ****************")
print("                                  Bem-vindo!                                    \n")

#Menu principal para encaminhar o utilizar para Disponibilidade ou Contabilidade

print("**************** Menu Administrador ****************")
print("1. Contabilidade\n2. Quartos disponiveis\n \nDigite 1 ou 2 para a opção pretendida.\n")

menuOpt = int(input())

#Caso o utilizador escolha a opção 1: Contabilidade. opção 2: Quartos disponiveis. Qualquer outra opção é inválida

#Ciclo no caso de o utilizador escolher a opção 1(Contabilidade):
#Menu de opção com quatro opções: Individual, duplo, triplo e suite. Qualquer escolha fora deste range é inválida.
if menuOpt == 1:
    print("Contabilidade...\n")
    print("**************** Contabilidade ****************")
    roomType = str(input("**** Qual o tipo de quarto? Escolha no menu: ****\nI. Individual ★\nD. Duplo ★\nT. Triplo ★\nS. Suite ★\n"))
    if roomType == "I" or roomType == "i":
            print("Escolheu Individual.")
    elif roomType == "D" or roomType == "d":
            print("Escolheu Duplo")
    elif roomType == "T" or roomType == "t":
            print("Escolheu triplo.")
    elif roomType == "S" or roomType == "s":
            print("Escolheu Suite.")
    else:
            print("Operação inválida. Escolha I, D, T ou S.")
            exit()

#Processo de input para os dias em que o quarto esteve reservado.
    roomDays = int(input("\nQuantos dias esteve o quarto reservado?\n"))


    if roomDays >=1 and roomDays <=365:
        print("O quarto esteve reservado", roomDays, "dias.")
    else:
        print("O intervalo de dias deve ser entre 1 e 365.")
        exit()





#Ciclo no caso de o utilizador escolher a opção 2:
elif menuOpt == 2:
    print("Quartos disponiveis...")

else:
    print("Operação inválida. Escolha opção 1 ou 2.") #







