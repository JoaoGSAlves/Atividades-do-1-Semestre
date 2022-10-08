def soma(x,y):
    return x+y 
def subtracao(x,y):
    return x-y
def multip(x,y):
    return x*y
def div(x,y):
    return x/y

print('*****CALCULADORA*****')
print('1- SOMA')
print('2- SUBTRAÇÃO')
print('3- MULTIPLICAÇÃO')
print('4- DIVISÃO')
print('5- SAIR')
n=int(input("DIGITE A OPERAÇÃO QUE DESEJA REALIZAR:"))
while n != 5:
    a=int(input("\nDigite o valor de X:"))
    b=int(input("\nDigite o valor de Y:"))
    if n == 1:
        print(f'\nSoma: {soma(a,b)}')
        n=int(input("\nDIGITE A PRÓXIMA OPERAÇÃO QUE DESEJA REALIZAR:"))
    if n == 2:
        print(f'\nSubtração: {subtracao(a,b)}')    
        n=int(input("\nDIGITE A PRÓXIMA OPERAÇÃO QUE DESEJA REALIZAR:"))
    if n == 3:
        print(f'\nMultiplicação: {multip(a,b)}')
        n=int(input("\nDIGITE A PRÓXIMA OPERAÇÃO QUE DESEJA REALIZAR:"))
    if n == 4:
        print(f'\nDivisão: {div(a,b)}')
        n=int(input("\nDIGITE A PRÓXIMA OPERAÇÃO QUE DESEJA REALIZAR:"))
    if n > 5:
        print('\nOPERAÇÃO INVÁLIDA, digite um número dentro de 1 a 5:')
        n=int(input("\nDIGITE A PRÓXIMA OPERAÇÃO QUE DESEJA REALIZAR:"))
    