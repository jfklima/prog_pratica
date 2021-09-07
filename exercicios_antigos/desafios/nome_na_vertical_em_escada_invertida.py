"""
Nome na vertical em escada invertida. Altere o programa anterior de
modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
"""

nome = list(input("Digite o seu nome: ").upper())

contador = len(nome)

for _ in range(contador):
    print(''.join(nome[:contador]))
    contador -= 1
