# Ex016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

'''from math import floor, trunc
n = float(input('Digite um número qualquer: '))
# print('O número {} tem sua parte inteira igual a {}'.format(n, floor(n)))
print('O número {} tem sua parte inteira igual a {}'.format(n, trunc(n)))'''

n = float(input('Digite um valor qualquer: '))
print('O valor digitado foi {} e sua parte inteira é {}'.format(n, int(n)))
