# Ex004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
# todas as informações possíveis sobre ela.

x = input('Digite algo: ')
# print(type(x), '{} é um número ({}), '.format(x, x.isnumeric()), '{} é alfabético ({})'.format(x, x.isalpha()))
print('O tipo primitivo de {} é {}'.format(x, type(x)))
print('Só tem espaços? ', x.isspace())
print('É um número? ', x.isnumeric())
print('É alfabético? ', x.isalpha())
print('É alfanumérico? ', x.isalnum())
print('Está em maiúsculas? ', x.isupper())
print('Está em minúsculas? ', x.islower())
print('Está capitalizada? ', x.istitle())
