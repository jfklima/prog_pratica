
from collections import Counter

"""
Apresenta quais são os caracteres de uma string e quantas vezes cada
caracter aparece na mesama.
"""
def contar_caracteres(s):
    """Função que conta os caracteres de uma string

    Ex:

    >>> contar_caracteres('renzo')
    {'e': 1, 'n': 1, 'o': 1, 'r': 1, 'z': 1}
    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, n: 2}

    :param s: string a ser contada

    """
    for caracter in s:
        resultado = dict(Counter(s).most_common())

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('renzo'))
    print()
    print(contar_caracteres('banana'))
