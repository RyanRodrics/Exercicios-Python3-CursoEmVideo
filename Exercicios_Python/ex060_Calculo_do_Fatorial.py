# Ex060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial

# Solução 1
n = int(input('Digite um número inteiro para calcular seu Fatorial: '))
c = n
f = 1
print('{}! ='.format(n), end=' ')
while c > 1:
    if c == 2:
        print('2 x 1 =', end=' ')
    else:
        print('{} x'.format(c), end=' ')
    f = f * c
    c = c - 1
if n == 0 or n == 1:
    print('1'.format(n))
elif n < 1:
    print('Tente novamente')
else:
    print('\033[34m{}\033[m'.format(f))

# Solução 2
c = n
f = factorial(n)
print('\n{}! ='.format(n), end=' ')
while c > 0:
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    c -= 1
print('\033[34m{}\033[m'.format(f))
