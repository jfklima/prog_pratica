lista = []

quantidade_de_produtos = int(input('Quantos produtos? '))


for i in range(quantidade_de_produtos):
    produtos_escolhidos = input('Produto escolhido: ')
    lista.append(produtos_escolhidos)



for i in range(produtos_escolhidos):
    preco_dos_produtos = input('Digite o preço do produto: ')
    lista.append(preco_dos_produtos)

print('O produto mais barato é:', min(lista))
