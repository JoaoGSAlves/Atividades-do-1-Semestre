# EXERCICIO 1 DA LISTA DE VETORES/ FEITO:

# vetor=[0]*10
# VETPOS=[0]*10
# VETNEG=[0]*10
# x=0
# for i in range (10):
#     vetor[i]= int(input('Informe os valores dos vetores:'))
#     if vetor[i] > 0:
#         VETPOS[i] += vetor[i] 
#     elif vetor[i] <0:
#         VETNEG[i] += vetor[i]
# print
# print(VETPOS)
# print(VETNEG)

# =-=-=-=-=--=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-=--=-=-=-==-=-=-=-
# EXERCICIO 2 DA LISTA DE VETORES/ NÃO FEITO:



# n=0
# count=0
# x= [0]*10
# vetor= [0]*10
# for i in range (10):
#     count+= 1
#     vetor[i]= int(input("Informe o %.d° valor: " %count))
#     if vetor[i] > x[i]:
#         x[i] += vetor[i]
# print(x) 


# =-=-=-=-=--=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-=--=-=-=-==-=-=-=-

# EXERCICIO 3 DA LISTA DE VETORES/FEITO :

# count=0
# x=[0]*15
# vetor= [0]*15
# for i in range (15):
#     count+= 1
#     vetor[i]= int(input("Informe o %.d° valor de um número Ímpar: " %count))
#     if vetor[i] % 2 == 1:
#         x[i] =+ vetor[i]
# print (x)

# =-=-=-=-=--=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-=--=-=-=-==-=-=-=-

# EXERCICIO 4 DA LISTA DE VETORES/ NÃO FEITO :


count=0
vetor= [0]*15
for i in range (15):
    count+= 1
    vetor[i]= int(input("Informe o %.d° valor de um número Ímpar: " %count))
    if vetor[i] < 0:
        vetor[i] = 0

print (vetor)