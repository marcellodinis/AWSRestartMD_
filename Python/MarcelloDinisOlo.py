#Mensagem de boas vindas ao utilizador.

print("**************** Sistema de reservas Hotel Notas Musicais ★★★★★ ****************")
print("                                  Bem-vindo!                                    \n")

#Menu principal para encaminhar o utilizar para Disponibilidade ou Contabilidade

print("**************** Menu Administrador ****************")
print("1. Contabilidade\n2. Quartos disponiveis\n \nDigite 1 ou 2 para a opção pretendida.\n")

menuOpt = int(input())

#Caso o utilizador escolha a opção 1: Contabilidade. opção 2: Quartos disponiveis. Qualquer outra opção é inválida
#Ciclo no caso de o utilizador escolher a opção 1(Contabilidade):
#Menu de opção com quatro opções: Individual, duplo, triplo e suite. Qualquer escolha fora deste range é inválida.
#Menu redundante. O utilizador pode selecionar o quarto pretendido com maiúscula ou minúscula.

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

    roomNum = int(input("\n► Escolha, por favor, o número do quarto desejado:\n"))

    if (roomNum == 2 or roomNum == 3 or roomNum == 5 or roomNum == 7 or roomNum == 11 or 
            roomNum == 13 or roomNum == 17 or roomNum == 19 or roomNum == 23 or roomNum == 29 or 
            roomNum == 31 or roomNum == 37 or roomNum == 41 or roomNum == 43 or roomNum == 47 or 
            roomNum == 53 or roomNum == 59 or roomNum == 61 or roomNum == 67 or roomNum == 71 or  
            roomNum == 73 or roomNum == 79 or roomNum == 83 or roomNum == 89 or roomNum == 97):
            print("O quarto",roomNum, "está disponível.")

    else:
            print("O quarto",roomNum, "não está disponível.")
            exit()

    #Processo de input para os dias em que o quarto esteve reservado.
    roomDays = int(input("\n► Quantos dias esteve o quarto reservado?\n"))

    #Condição genérica para confirmar se o input do utilizador é válido.
    if roomDays >=1 and roomDays <=365:
            print("\n► O quarto esteve reservado", roomDays, "dias.\n")
    else:
            print("O intervalo de dias deve ser entre 1 e 365.")
            exit()



    #Lógica para tipo de quarto individual (Diária: 200€ | Limpeza: 15€ dia | Tributação variável 23/25/28%)
    if roomType == "I" or roomType == "i":
                dailyCostI = (roomDays * 200) # var dailyCost multiplica com a taxa fixa de 200€/dia para obter valor total
                tidyCostI = (roomDays * 15) # var tidyCostI multiplica com a taxa fixa de 15€/dia que deve subtrair ao valor total.
                
                if (dailyCostI <= 20000):
                                taxCostI = (dailyCostI * 0.23) # até 20.000€ var taxCostI multiplica com 0.23(23%) para obter valor de tributação.
                                print("● Rendeu um valor bruto de", dailyCostI,"€.")
                                print("● O valor total com a limpeza foi de", tidyCostI,"€.")
                                print("● É entregue ao estado", taxCostI,"€.")  
                                print("● Lucro total:", dailyCostI - tidyCostI - taxCostI,"€.\n")

                if (dailyCostI > 20000 and dailyCostI <= 50000):
                                taxCostI = (dailyCostI * 0.25)
                                print(dailyCostI)
                                print(tidyCostI)
                                print(taxCostI)  
                                print(dailyCostI - tidyCostI - taxCostI)

                if (dailyCostI > 50000):
                                taxCostI = (dailyCostI * 0.28)
                                print(dailyCostI)
                                print(tidyCostI)
                                print(taxCostI)  
                                print(dailyCostI - tidyCostI - taxCostI)
    

    #Lógica para tipo de quarto duplo (Diária: 250€ | Limpeza: 20€ dia | Tributação variável 23/25/28%)
    if roomType == "D" or roomType == "d":
                dailyCostI = (roomDays * 250) # var dailyCost multiplica com a taxa fixa de 250€/dia para obter valor total
                tidyCostI = (roomDays * 20) # var tidyCostI multiplica com a taxa fixa de 20€/dia que deve subtrair ao valor total.
                
                if (dailyCostI <= 20000):
                                taxCostI = (dailyCostI * 0.23) # até 20.000€ var taxCostI multiplica com 0.23(23%) para obter valor de tributação.
                                print("● Rendeu um valor bruto de", dailyCostI,"€.")
                                print("● O valor total com a limpeza foi de", tidyCostI,"€.")
                                print("● É entregue ao estado", taxCostI,"€.")  
                                print("● Lucro total:", dailyCostI - tidyCostI - taxCostI,"€.\n")

                if (dailyCostI > 20000 and dailyCostI <= 50000):
                                taxCostI = (dailyCostI * 0.25)
                                print(dailyCostI)
                                print(tidyCostI)
                                print(taxCostI)  
                                print(dailyCostI - tidyCostI - taxCostI)

                if (dailyCostI > 50000):
                                taxCostI = (dailyCostI * 0.28)
                                print(dailyCostI)
                                print(tidyCostI)
                                print(taxCostI)  
                                print(dailyCostI - tidyCostI - taxCostI)


    #Lógica para tipo de quarto triplo (Diária: 275€ | Limpeza: 20€ dia | Tributação variável 23/25/28%)
    if roomType == "T" or roomType == "t":
                dailyCostI = (roomDays * 275) # var dailyCost multiplica com a taxa fixa de 275€/dia para obter valor total
                tidyCostI = (roomDays * 20) # var tidyCostI multiplica com a taxa fixa de 20€/dia que deve subtrair ao valor total.
                
                if (dailyCostI <= 20000):
                                taxCostI = (dailyCostI * 0.23) # até 20.000€ var taxCostI multiplica com 0.23(23%) para obter valor de tributação.
                                print("● Rendeu um valor bruto de", dailyCostI,"€.")
                                print("● O valor total com a limpeza foi de", tidyCostI,"€.")
                                print("● É entregue ao estado", taxCostI,"€.")  
                                print("● Lucro total:", dailyCostI - tidyCostI - taxCostI,"€.\n")

                if (dailyCostI > 20000 and dailyCostI <= 50000):
                                taxCostI = (dailyCostI * 0.25)
                                print(dailyCostI)
                                print(tidyCostI)
                                print(taxCostI)  
                                print(dailyCostI - tidyCostI - taxCostI)

                if (dailyCostI > 50000):
                                taxCostI = (dailyCostI * 0.28)
                                print(dailyCostI)
                                print(tidyCostI)
                                print(taxCostI)  
                                print(dailyCostI - tidyCostI - taxCostI)


    #Lógica para tipo de quarto suite (Diária: 350€ | Limpeza: 30€ dia | Tributação variável 23/25/28%)
    if roomType == "S" or roomType == "s":
                dailyCostI = (roomDays * 350) # var dailyCost multiplica com a taxa fixa de 350€/dia para obter valor total
                tidyCostI = (roomDays * 30) # var tidyCostI multiplica com a taxa fixa de 30€/dia que deve subtrair ao valor total.
                
                if (dailyCostI <= 20000):
                                taxCostI = (dailyCostI * 0.23) # até 20.000€ var taxCostI multiplica com 0.23(23%) para obter valor de tributação.
                                print("● Rendeu um valor bruto de", dailyCostI,"€.")
                                print("● O valor total com a limpeza foi de", tidyCostI,"€.")
                                print("● É entregue ao estado", taxCostI,"€.")  
                                print("● Lucro total:", dailyCostI - tidyCostI - taxCostI,"€.\n")

                if (dailyCostI > 20000 and dailyCostI <= 50000):
                                taxCostI = (dailyCostI * 0.25)
                                print(dailyCostI)
                                print(tidyCostI)
                                print(taxCostI)  
                                print(dailyCostI - tidyCostI - taxCostI)

                if (dailyCostI > 50000):
                                taxCostI = (dailyCostI * 0.28)
                                print(dailyCostI)
                                print(tidyCostI)
                                print(taxCostI)  
                                print(dailyCostI - tidyCostI - taxCostI)



#Ciclo no caso de o utilizador escolher a opção 2. Mostrar quartos vagos (números primos, falta fórmula)
elif menuOpt == 2:
                print("\n**************** Quartos disponiveis ****************")
                print("\n► Estão disponíveis os quartos: \n2, 3, 5, 7, 11, 13, 17, 19, 23\n29, 31, 37, 41, 43, 47, 53, 59\n61, 67, 71, 73, 79, 83, 89 e 97.\n")
                

else:
                print("\nOperação inválida. Escolha opção 1 ou 2.") #