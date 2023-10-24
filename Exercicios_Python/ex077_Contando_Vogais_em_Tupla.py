# Ex077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

tupla = ('Sorvete', 'Chocolate', 'Bolo', 'Pudim', 'Mousse', 'Suco', 'Biscoito')
print('As palavras são: ', tupla)

for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra} ', end='')
