# Ex023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus dígitos separados.

n = int(input('Digite um número de 0 a 9999: '))
# numero = str(n)
print('Sobre o número {}, temos que:'.format(n))
# print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(numero[3], numero[2], numero[1], numero[0]))
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u, d, c, m))
