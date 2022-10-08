vetor=[0]*5
valor=0
for i in range(5):
    vetor[i]= int(input('\nInforme o valor: '))
    if vetor[i] > valor:
        valor += vetor[i]
        valor=vetor[i]
print (valor)