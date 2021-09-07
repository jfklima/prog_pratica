nota = float(input("Digite uma nota ou -1 para sair: "))
notas = []

while True:
    if nota == -1.0:
        break

    notas.append(nota)
    nota = float(input("Digite uma nota ou -1 para sair: "))

soma = sum(notas)
contador = len(notas)
media = soma / contador

print()
print(f"Quantidade de notas lidas: {contador}")
print("Notas:")

print(' '.join([str(nota) for nota in notas]))

acima_da_media = 0
notas_abaixo_de_sete = 0

notas.reverse()
for nota in notas:
    if nota > media:
        acima_da_media += 1
    if nota < 7:
        notas_abaixo_de_sete += 1
    print(nota)

print(f"Soma das notas: {soma}")
print(f"Média das notas: {media}")
print(f"Quantidade de notas acima da média: {acima_da_media}")
print(f"Quantidade de notas abaixo de 7: {notas_abaixo_de_sete}")
print()
print("Obrigado por usar a nossa plataforma!")