
n = int(input("Quantidade de casos de teste: "))
for cont in range(1,n+1):
    x = int(input())
    if 10 <= x <= 20:
        print(" Valor dentro do Intervalo de [10 e 20] = In ")
    else:
        print(" Valor fora do Intervalo de [10 e 20] = Out ")