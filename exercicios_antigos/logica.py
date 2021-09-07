linguas = {
    'bra': 'portugues',
    'eua': 'ingles',
    'esp': 'espanhol',
}

idiomas = {}

# idiomas['bra'] = linguas.pop('bra')

print(idiomas)
print(linguas)
print()

pais, idioma = linguas.popitem()
idiomas[pais] = idioma

print(idiomas)
print(linguas)
print()

pais, idioma = linguas.popitem()
idiomas[pais] = idioma

print(idiomas)
print(linguas)
print()

pais, idioma = linguas.popitem()
idiomas[pais] = idioma

print(idiomas)
print(linguas)
print()
