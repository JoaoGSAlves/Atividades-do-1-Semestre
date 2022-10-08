def funcao():
    n1 = float(input(" Escreva a nota da sua Primeira Avaliação: "))
    n2 = float(input(" Escreva a nota da sua Segunda Avaliação: "))
    media = (n1 + n2) /2 
    print("Sua média é %.2f:" %(media))
    if media >=6:
        print(" Você está Aprovado!")
    else:
        print(" Você está de Recuperação!" )
funcao()
while True:
    pergunta = input("Você quer refazer o cálculo da sua nota [S/N]:")
    if pergunta == 'S' or pergunta == 's':
            funcao()
    elif pergunta == 'n' or pergunta == 'N':
            print("Fim")
            break
