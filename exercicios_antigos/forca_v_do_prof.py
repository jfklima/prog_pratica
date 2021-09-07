"""
file: forca_v_do_prof.py

Um Jogo da Forca simple mais funcional

"""

palavra = 'DevPro'.upper()

print("Jogo da Forca")
print("Descubra a palavra")

conjunto_letras_palavra = set(palavra)
conjunto_letras_digitadas = set()
erros = 0

while not conjunto_letras_palavra.issubset(conjunto_letras_digitadas) and erros < 7:
    print()
    print()

    letra_digitada = input("Digite uma letra: ").upper()

    conjunto_letras_digitadas.add(letra_digitada)

    if letra_digitada in conjunto_letras_palavra:
        print("Palavra é: ", end='')

        for letra in palavra:
            if letra in conjunto_letras_digitadas:
                print(f"{letra} ", end='')
            else:
                print("_ ", end='')
        print()
        print()
    else:
        erros += 1
        print(f"Você errou {erros} de 6, tente outra vez!")

    print("Letras já digitadas: ", conjunto_letras_digitadas)

if erros < 7:
    print("Parabéns Você Ganhou")
else:
    print("Infelismente Você perdeu")
