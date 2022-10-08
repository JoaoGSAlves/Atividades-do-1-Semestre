print("\n ========================================================================= ")
print("\n Qual tipo de Combustível você utilizará para reabastecer seu Automóvel? \n")
print(" 1 - Álcool")
print(" 2 - Gasolina")
print(" 3 - Diesel")
print (" Digite 4 para encerrar sua pesquisa!!\n")
x = int(input("Digite a forma de reabastecimento utilizada:\n"))
alcool=0
gasolina=0
diesel=0
invalido=0
fim=4
while x != 4:
    if x == 1:
        alcool = alcool+1
        x = int(input("Digite a forma de reabastecimento utilizada:\n"))
    elif x == 2:
        gasolina = gasolina +1
        x = int(input("Digite a forma de reabastecimento utilizada:\n"))
    elif x == 3:
        diesel = diesel +1
        x = int(input("Digite a forma de reabastecimento utilizada:\n"))
    elif x >= 5 or x == 0:
        invalido= invalido+1
        print("\n************************************************************************************************************")
        print(" \nEsse número não é valido, por favor utilize a numeração de 1 a 3 e o número 4 para encerrar a pesquisa!\n")
        x = int(input("\nDigite a forma de reabastecimento utilizada:\n"))

print("\n MUITO OBRIGADO!!!")
print(" Alcool: %i" %alcool)
print(" Gasolina: %i" %gasolina)    
print(" Diesel: %i" %diesel)

