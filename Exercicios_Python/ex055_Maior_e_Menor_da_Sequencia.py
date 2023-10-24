# Ex055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

peso = 0
maior = 0
menor = 0
print('Digite o peso de 5 pessoas: ')
for p in range(1, 6):
    peso = float(input('{}°: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso digitado foi \033[31m{} kg\033[m, e o menor foi \033[33m{} kg\033[m'.format(maior, menor))
