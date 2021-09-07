# faça um programa que leia duas strings e informe o conteúdo delas seguido do
# seu comprimento, informe também se as duas strings possuem o mesmo
# comprimento e se são iguais ou diferentes no conteúdo.

str_A = input("Digite uma string: ")
str_B = input("Digite outra string: ")

comprimento_A = len(str_A)
comprimento_B = len(str_B)

print(str_A)
print(str_B)

print(f"Comprimento de str_A {comprimento_A} caracteres")
print(f"Comprimento de str_B {comprimento_B} caracteres")

comparacao_de_tamanho = 'diferentes'
comparacao_de_conteudo = 'diferentes'

if str_A == str_B:
    comparacao_de_tamanho = 'iguais'
    comparacao_de_conteudo = 'iguais'
elif comprimento_A == comprimento_B:
    comparacao_de_tamanho = 'iguais'

print(f"São iguais no seu comprimento: {comparacao_de_tamanho}")
print(f"São iguais no seu conteúdo: {comparacao_de_conteudo}")
