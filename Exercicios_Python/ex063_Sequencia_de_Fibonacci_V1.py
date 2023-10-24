# Ex063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci.

print('\033[33m-\033[m' * 25)
print('\033[36mSequência de Fibonacci\033[m')
print('\033[33m-\033[m' * 25)
n = int(input('Deseja ver quantos termos? \033[34m'))
a1 = 1
a2 = 1
s = 0
c = 0

while c < n:
    if c == 0:
        print(c, '-->', end=' ')
    elif 0 < c <= 2:
        print(a1, '-->', end=' ')
    else:
        s = a1 + a2
        print(s, '-->', end=' ')
        a1 = a2
        a2 = s
    c += 1
print('FIM')
