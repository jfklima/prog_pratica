"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar
o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO

"""
nome = input("Digite o seu nome: ").upper()

letras = list(nome)
for indice in range(len(nome)):
    palavra = ''.join(letras[:indice])
    print(palavra)

palavra = ''.join(letras[:len(letras) + 1])
print(palavra)
