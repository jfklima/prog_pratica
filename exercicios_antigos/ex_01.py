"""Criar uma função que retorne min e max de uma sequência numérica
aleatória.

Só pode usar if, comparações, recursão e funções que sejam de sua
autoria.

Se quiser usar laços também pode.

Deve informar via docstring qual é a complexidade de tempo e espaço da
sua solução
"""

from math import inf


def minimo_e_maximo(sequencia_numerica):
    ''' Retorna o minimo e o maximo de uma sequência numérica aleatória.

    Complexidade:
        execução: O(n)
        espaço: O(3)
    '''

    maximo = -inf  # 1
    minimo = +inf  # 1

    for elem in sequencia_numerica:  # 1
        if elem > maximo:  # 2
            maximo = elem  # 1
        if elem < minimo:  # 2
            minimo = elem  # 2
    return minimo, maximo  # 1


def recursivo_minmax(sequencia_numerica):

    def r_minimo(sequencia):
        primeiro = sequencia[0]

        if len(sequencia) == 1:
            return primeiro
        else:
            menor = r_minimo(sequencia[1:])
            return menor if menor < primeiro else primeiro

    def r_maximo(sequencia):
        primeiro = sequencia[0]

        if len(sequencia) == 1:
            return primeiro
        else:
            maior = r_maximo(sequencia[1:])
            return maior if maior > primeiro else primeiro

    return r_minimo(sequencia_numerica), r_maximo(sequencia_numerica)


def recursivo_minmax_1x(sequencia_numerica):
    primeiro = sequencia_numerica[0]
    if len(sequencia_numerica) == 1:
        return primeiro, primeiro
    else:
        return

# print(minimo_e_maximo([1, 2, 3, 4]))
# print(minimo_e_maximo([1, 3, 10, 12, 44, 2, 24, 25]))
# print(minimo_e_maximo([88, 66, 10, 2, 8]))


print(recursivo_minmax([1, 2, 3, 4]))
