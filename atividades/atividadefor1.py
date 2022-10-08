x = int(input( "Informe o valor de X: "))
if x < 0 or x > 1000:
      print('Valor inválido! ')
for cont in range(1,x+1,2):
    print(cont)
    if x >= 1000:
        break