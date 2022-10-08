def area(n):
    return 3.14*n*n

def perimetro(n):
    return 3.14*2*n

x=int(input("\nDIgite o raio do círculo que deseja calcular a AREA e PERIMETRO: "))
print("=-"*35)
print(f'\nAREA: {area(x)}')
print(f'\nPERIMETRO: {perimetro(x)}' )

