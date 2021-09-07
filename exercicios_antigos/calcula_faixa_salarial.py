salarios = [200, 250, 320, 413, 516, 680, 791, 877, 999, 1000, 2000, 3000]

# contagem de faixa salarial
vetor_de_contagem = [0] * 9


for salario in salarios:
    indice = salario // 100 - 2
    indice_maximo = len(vetor_de_contagem) - 1
    indice = min(indice, indice_maximo)
    vetor_de_contagem[indice] += 1


print(vetor_de_contagem)
