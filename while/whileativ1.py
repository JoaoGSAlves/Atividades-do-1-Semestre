soma = 0
cont = 0
idade = int(input("Informe uma idade - digite um valor negativo para finalizar: "))
while idade>=0:
    soma= soma + idade
    cont= cont + 1
    idade = int(input("Informe uma idade - digite um valor negativo para finalizar: "))
if cont > 0:
    media=soma/cont
    print('Média das idades: %.2f' %(media))
else:
    print('Nenhuma idade informada! ')