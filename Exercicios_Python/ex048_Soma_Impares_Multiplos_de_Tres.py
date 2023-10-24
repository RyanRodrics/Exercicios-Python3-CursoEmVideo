# Ex048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram
# no intervalo de 1 até 500.

print('A soma de todos os números \033[36mímpares\033[m \033[32mmúltiplos de 3\033[m de \033[31m1 a 500\033[m é:')
s = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        s = s + c
print('{}{}{}'.format('\033[33m', s, '\033[m'))

# solução 2
print('\nSolução 2')
sn = 0
cont = 0
for n in range(3, 501, 6):
    sn += n   # sn = sn + n
    cont += 1   # cont = cont + 1
print('Foram {} números, cuja soma é {}'.format(cont, sn))
