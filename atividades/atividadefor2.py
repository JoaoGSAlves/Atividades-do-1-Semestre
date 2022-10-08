n = int(input(" Informe o valor de N :"))
if n < 0 or n > 10000:
      print('Valor Inválido')
for cont in range(1,10001,):
    if cont % n == 2:
        print(cont)
