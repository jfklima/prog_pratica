# Faça um programa que permita ao usuário digitar o seu nome em seguida mostre
# o nome do usuário de traz para frente utilizando somente letras maiúsculas.

nome = 'Franklin Lima'.upper()

nome_invertido_por_letras = ''.join(reversed(nome))

nome_invertido_por_palavras = ' '.join(reversed(nome.split()))
print(f"Nome com letras em maiúscula: {nome}")
print(f"Nome com letras em maiúscula invertida por letras: {nome_invertido_por_letras}")
print(f"Nome com letras em maiúscula invertida por palavras: {nome_invertido_por_palavras}")
