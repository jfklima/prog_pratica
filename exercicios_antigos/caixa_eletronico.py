# Faça um Programa para um caixa eletrônico. O programa deverá perguntar
# ao usuário o valor do saque e depois informar quantas notas de cada
# valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50
# e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O
# programa não deve se preocupar com a quantidade de notas existentes na
# máquina.

# a) Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas
#    de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

# b) Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
#    três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e
#    quatro notas de 1.

from random import randint

valor = 256
valor = 399
valor = 989

aleatorio = randint(1, 10)

# nota_100_str = nota_50_str = nota_20_str = nota_10_str = nota_5_str = nota_1_str = '


nota_100_int, valor = divmod(valor, 100)
nota_50_int, valor = divmod(valor, 50)
nota_20_int, valor = divmod(valor, 20)
nota_10_int, valor = divmod(valor, 10)
nota_5_int, nota_1_int = divmod(valor, 5)
# nota_1_int, valor = divmod(valor, 1)

ordinais = {
    1: "uma",
    2: "duas",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
}

if nota_100_int > 0:
    print(f"{nota_100_int} nota(s) de 100")

if nota_50_int > 0:
    print(f"{nota_50_int} nota(s) de 50")

if nota_20_int > 0:
    print(f"{nota_20_int} nota(s) de 20")

if nota_10_int > 0:
    print(f"{nota_10_int} nota(s) de 10")

if nota_5_int > 0:
    print(f"{nota_5_int} nota(s) de 5")

if nota_1_int > 0:
    print(f"{nota_1_int} nota(s) de 1")
