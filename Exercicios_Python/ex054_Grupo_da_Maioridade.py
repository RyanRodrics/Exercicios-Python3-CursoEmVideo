# Ex054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.

from datetime import date
maiores = 0
menores = 0
print('Digite o ano de nascimento de pessoas')
for c in range(1, 8):
    nasc = int(input('({}°): '.format(c)))
    if date.today().year - nasc >= 18:
        maiores += 1
    elif date.today().year - nasc < 18:
        menores += 1
print('Dessas 7 pessoas, \033[32m{}\033[m são maiores de idade '
      'e \033[32m{}\033[m são menores de idade'.format(maiores, menores))
