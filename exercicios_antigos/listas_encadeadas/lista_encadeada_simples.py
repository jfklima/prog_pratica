'''
Definição - Lista Encadeada

- Lista com alocação dinâmica de memória.
- Não ocupam posição contíqua em memória.
- Baseada em estrutura de Nó (Noh).

'''


class Noh:
    """Cada Nó quarda um valor e referência para um ou mais Nós."""

    def __init__(self, valor, ref):
        self.valor = valor
        self.ref = ref
