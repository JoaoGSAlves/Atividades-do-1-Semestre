notas= [0]*5
media=0
qtde=0
for i in range(5):
    notas[i]=float(input('Informe a nota: '))
    media = media + notas[i]
media = media /5

for i in range(5):
    if(notas[i]>media):
        qtde= qtde + 1
print("\nMédia da turma: %.1f\n" %media)
print('Notas acima da média: %d' %qtde)