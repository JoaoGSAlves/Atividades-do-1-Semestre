def celcius(f):
    c = 5/9*(f-32)
    return c

x = int(input("Digite um valor em Farheint: "))
print('A conversão de %d° Farheint para Celsius é: %d' %(x,celcius(x)))