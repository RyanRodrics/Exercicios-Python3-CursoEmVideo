# Ex059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
print('Digite dois valores:')
n1 = float(input('Primeiro valor --> '))
n2 = float(input('Segungo valor --> '))
o = 0
maior = 0
print('''Escolha uma das opções abaixo\033[34m
[1] Somar
[2] Multiplicar
[3] Verificar qual o maior
[4] Mudar para novos valores
[5] Sair do programa\033[m''')
while o != 5:
    o = int(input('Sua opção: '))
    if o == 1:
        print('{} + {} = \033[31m{}\033[m\n'.format(n1, n2, n1 + n2))
    if o == 2:
        print('{} X {} = \033[31m{}\033[m\n'.format(n1, n2, n1 * n2))
    if o == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        print('O maior valor é \033[31m{}\033[m\n'.format(maior))
    if o == 4:
        n1 = float(input('Novo primeiro valor --> '))
        n2 = float(input('Novo segundo valor --> '))
        print(' ')
    if o == 5:
        print('\033[35mSaindo\033[m...')
        sleep(1.5)
    if o != 1 and o != 2 and o != 3 and o != 4 and o != 5:
        print('\033[31mOpção inválida! Tente novamente\033[m\n')
print('\n\033[32mObrigado por participar :D')
