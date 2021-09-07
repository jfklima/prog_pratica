# Criar o jogo da forca

# O jogador poderá errar 6 vezes antes de ser inforcado

palavra_secreta = 'caso'
espacos = ' '.join(["_"] * len(palavra_secreta))

tentativa = 1
# import pdb; pdb.set_trace()
while tentativa <= 6:
    letra = input("Digite uma letra: ")

    if letra in palavra_secreta:
        print(palavra_secreta.index(letra))
        indice = palavra_secreta.index(letra)
        espaco = espaco[indice:-1] = [letra] + espaco[indice:]
    else:
        print(f"Você errou pela {tentativa}o Vez. Tente de novo!")
        if tentativa == 6:
            break
        tentativa += 1


print("Game Over!!!")
