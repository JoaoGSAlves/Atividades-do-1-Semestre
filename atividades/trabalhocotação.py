print("=====================================")
def funcao():
    dolar = float(input("Quantos dólares deseja converter?"))
    cotacao = float(input("Qual a cotação atual do dólar?"))
    real= dolar*cotacao
    print("Você tem %.2f reais!" %(real))
funcao()
while True:
    pergunta = input("Você quer refazer o cálculo da sua nota [S/N]:")
    if pergunta == 'S' or pergunta == 's':
            funcao()
    elif pergunta == 'n' or pergunta == 'N':
            print("Fim")
            break