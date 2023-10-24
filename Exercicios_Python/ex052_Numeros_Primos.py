# Ex052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro: '))
divisores = 0
for c in range(1, n + 1):
    if n % c == 0:
        divisores += 1
        print('{}{}{}'.format('\033[33m', c, '\033[m'), end=' ')
    else:
        print('{}{}{}'.format('\033[31m', c, '\033[m'), end=' ')
if divisores == 2:
    print('\nO número \033[34m{}\033[m tem apenas 2 divisores, então é primo'.format(n))
else:
    print('\nO número \033[34m{}\033[m tem {} divisores, então não é primo'.format(n, divisores))
