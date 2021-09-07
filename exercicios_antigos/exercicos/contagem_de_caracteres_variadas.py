from collections import Counter

"""
Apresenta quais são os caracteres de uma string e quantas vezes cada
caracter aparece na mesama.
"Função que conta os caracteres de uma string

Ex:

>>> contar_caracteres('renzo')
{'e': 1, 'n': 1, 'o': 1, 'r': 1, 'z': 1}
>>> contar_caracteres('banana')
{'a': 3, 'b': 1, n: 2}

:param s: string a ser contada

"""
def cont_char(s):
    char_uniq=set(s)
    result = {}

    for c in char_uniq:
        result[c] = s.count(c)

    return result


def contar_caracteres(s: str) -> dict:
    return dict(Counter(s))


def contar(palavra):
    ordenada = sorted(set(palavra))
    result = [(caracteres, palavra.count(caracteres)) for caracteres in ordenada]
    return result

if __name__ == '__main__':
    # print(cont_char('banana'))
    print(contar_caracteres('banana'))
    # print(contar('banana'))
