# soma = 0
# cont = 0
# idade = int(input("Informe uma idade - digite um valor negativo para finalizar: "))
# while idade>=0:
#     soma= soma + idade
#     cont= cont + 1
#     idade = int(input("Informe uma idade - digite um valor negativo para finalizar: "))
# if cont > 0:
#     media=soma/cont
#     print('Média das idades: %.1f' %(media))
# else:
#     print('Nenhuma idade informada! ')
def funcao():
    print('\n**** SOMA ****')
    n1= int(input("\nInforme o Primeiro Valor: "))
    n2= int(input("\nInforme o Segundo Valor: "))
    soma = n1+n2
    print("\nSoma: %.d" %(soma))
funcao()
while True:
    pergunta = input("Você quer refazer o cálculo da sua nota [S/N]:")
    if pergunta == 'S' or pergunta == 's':
            funcao()
    elif pergunta == 'n' or pergunta == 'N':
            print("Fim")
            break

# resp = input('Deseja informar um valor para o cálculo do quadrado (s - sim ou n - não)?')
# while resp == "S" or resp == "s":
#     funcao()
#     resp = input('Deseja informar um valor para o cálculo do quadrado (s - sim ou n - não)?')




