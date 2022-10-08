# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

# Código da cidade;
# Número de veículos de passeio (em 2021);
# Número de acidentes de trânsito com vítimas (em 2021).

# Deseja-se saber:

# Qual a quantidade total de veículos entre as cinco cidades;
# Qual o número médio de acidentes de trânsito nas cidades com até 2.000 veículos de passeio.


# codigoCidade = int(input("Digite o código da cidade: "))
# quantVeiculos = int(input("Digite o número de veículos na cidade: "))
# quantAcidentes = int(input("Digite o número de acidentes com vitimas da cidade: "))
# print("")

# indiceAcidente = float(quantAcidentes) / quantVeiculos
# maiorIndice = indiceAcidente
# maiorIndiceCodigo = codigoCidade
# menorIndice = indiceAcidente
# menorIndiceCodigo = codigoCidade
# soma = quantVeiculos
# somaVeiculos2000 = 0
# divisorMedia2000 = 1

# if (quantVeiculos < 2000):
# 	somaVeiculos2000 = somaVeiculos2000 + quantAcidentes
# 	divisorMedia2000 = divisorMedia2000 + 1

# a = 1
# while (a < 5):
# 	codigoCidade = int(input("Digite o código da cidade: "))
# 	quantVeiculos = int(input("Digite o número de veículos na cidade: "))
# 	quantAcidentes = int(input("Digite o número de acidentes com vítimas da cidade: "))
# 	print("")
# 	indiceAcidente = float(quantAcidentes) / quantVeiculos
# 	soma = soma + quantVeiculos

# 	if (indiceAcidente > maiorIndice):
# 		maiorIndice = indiceAcidente
# 		maiorIndiceCodigo = codigoCidade

# 	if (indiceAcidente < menorIndice):
# 		menorIndice = indiceAcidente
# 		menorIndiceCodigo = codigoCidade

# 	if (quantVeiculos < 2000):
# 		somaVeiculos2000 = somaVeiculos2000 + quantAcidentes
# 		divisorMedia2000 = divisorMedia2000 + 1

# 	a = a + 1

# print("\nMenor índice: %.2f \nCódigo da cidade: %d" % (menorIndice, menorIndiceCodigo))
# print("\nMaior índice: %.2f \nCódigo da cidade: %d" % (maiorIndice, maiorIndiceCodigo))
# print("Média de veículos nas %d cidades = %d veículos" % (a,(float(soma)/a)))

# Definindo as variáveis
maior = menor = count = soma_veiculos = soma_acidentes = soma_2k = 0
cid_maior = cid_menor = ''

# Laço para que o usuário digite os dados das 5 cidades 
for c in range(1,6):
    cidade      = str(input("\nDigite o nome da cidade.....................: "))
    codigo      = int(input("Digite o código da cidade...................: "))
    veiculos    = int(input("Numero de veiculos de passeio...............: "))
    acidentes   = int(input("Numero de acidentes de transito com vitimas.: "))

    soma_veiculos += veiculos
    soma_acidentes += acidentes

    if acidentes > maior:
        maior = acidentes
        cid_maior = cidade

    if acidentes < menor or c == 1:
        menor = acidentes
        cid_menor = cidade

    if veiculos < 2000:
        soma_2k += acidentes
        count += 1

# Calculando a média das 5 cidades
media_nas_5_cidades = soma_veiculos / c
media_2k = soma_2k / count

# Exibindo os resultados
print("\n"+"-="*30)
print(f"O menor indice de acidentes de transito {menor} cidade que pertence {cid_menor}")
print(f"O maior indice de acidenstes de transito {maior} cidade que pertence {cid_maior}")
print(f"Media de veiculos nas cincos cidades {media_nas_5_cidades}")
print(f"Media de acidentes de transitos nas cidades com menos de 2000 é {media_2k}") 