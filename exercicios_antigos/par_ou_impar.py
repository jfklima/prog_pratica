# file: par_ou_impar
#
# Verifica se o valor é par ou impar.

while True:
    banana = input('Em qual número você está pensando? ')

    if banana == 'exit':
        break
        print('hello')

    if banana.isnumeric() and int(banana) in range(1, 1000):
        numero = int(banana)

        if numero % 2 == 0:
            print(f'{numero} é par! Tem outro?')
        else:
            print(f'{numero} ímpar! Tem outro?')
    else:
        print('Digite um número')
