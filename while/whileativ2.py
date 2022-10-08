# n = int(input("Digite um número inteiro positivo: "))
# for divisor in range(1, n+1):
#     if n % divisor == 0:
#         print(divisor)

n = int(input(" Informe um número N para o programa calcular seus divisores: "))
s =0
while s < n:
    s += 1
    m = n/s
    if n % s == 0:
        print (m)
