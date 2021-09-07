
"""
Apresenta quais são os caracteres de uma string e quantas vezes cada
caracter aparece na mesama.
"""
from pprint import pprint

def contar_caracteres(s):
    """Função que conta os caracteres de uma string

    Ex:

    >>> contar_caracteres('renzo')
    {'e': 1, 'n': 1, 'o': 1, 'r': 1, 'z': 1}
    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, n: 2}

    :param s: string a ser contada

    """
    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado

if __name__ == '__main__':
    pprint(contar_caracteres('renzo'))
    print()
    pprint(contar_caracteres('goiaba'))
