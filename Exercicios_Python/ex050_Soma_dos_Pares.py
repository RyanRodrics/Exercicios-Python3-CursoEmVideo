# Ex050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

s = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print('A \033[31msoma\033[m dos números \033[36mpares\033[m digitados é \033[32m{}\033[m'.format(s))
