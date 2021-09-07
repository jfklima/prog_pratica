import pytest

def soma(a, b):
    return a + b

def test_soma_com_valores_maiores_que_1():
    assert soma(0, 1) == 1

produtos = {}

quantidade_de_produtos = int(input("Quantos produtos? "))


for _ in range(quantidade_de_produtos):
    produto = input('Produto escolhido: ')
    preco = float(input(f'Preço {produto}: '))
    produtos[produto] = preco


menor_preco = min(produtos.values())
produto_menor_preco = ''


for produto, preco in produtos.items():
    if preco == menor_preco:
        produto_menor_preco = produto


print(f'Pruduto mais barato: {produto_menor_preco} , Preço: R$ {menor_preco}')
