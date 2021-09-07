


""" CARTÃO DE CREDITO - FATURA EM DIA / ATRASADO"""
valor_original = 278
taxa = 0.05
juros_diarios = 0.002
dia_pagamento = 28
dia_vencimento = 25
dias_de_atraso = dia_pagamento - dia_vencimento

cliente = {'nome': 'Bruno', 'sobrenome': 'Jatobá'}

def adimplente_inadiplente (**cliente):
    print (**cliente)
print (cliente)

def fatura_emdia_vencida(*args):
    if dia_pagamento > dia_vencimento:
        ac = valor_original
        for n in args:
            ac += n
        return ac
    elif dia_pagamento <= dia_vencimento:
        ac = valor_original
        for n in args:
            ac = n
        return ac

if dia_pagamento > dia_vencimento:
    print(fatura_emdia_vencida(valor_original * taxa, valor_original * juros_diarios * dias_de_atraso))
    print ('Evite o bloqueio do seu cartão. Entre em contato conosco: 0800 789 8874')
elif dia_pagamento <= dia_vencimento:
    print(valor_original)
    print('Parabens!!! Voce esta em dia')
