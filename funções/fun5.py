def divisores(n):
    for i in range(1,n):
        if n % i == 0:
            print(i)

x = [0]*10
for i in range (10):
    x[i]=int(input("Digite os valores:"))
    print('O número %d e seus divsores são %d'%(x,divisores(x)))