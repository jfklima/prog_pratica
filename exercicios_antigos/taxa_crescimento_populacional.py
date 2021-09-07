numero_de_anos = 0
populacao_pais_A = 80_000
populacao_pais_B = 200_000
taxa_crescimento_pais_A = 3
taxa_crescimento_pais_B = 1.5

while populacao_pais_A < populacao_pais_B:
    crescimento_pais_A = taxa_crescimento_pais_A / 100 * populacao_pais_A
    crescimento_pais_B = taxa_crescimento_pais_B / 100 * populacao_pais_B

    populacao_pais_A += crescimento_pais_A
    populacao_pais_B += crescimento_pais_B
    numero_de_anos += 1

print(f"Número de anos: {numero_de_anos}")
print(f"Populacao país A: {populacao_pais_A:.2f}")
print(f"Populacão país B: {populacao_pais_B:.2f}")
