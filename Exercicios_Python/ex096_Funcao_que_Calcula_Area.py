# Ex096: aça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {l}x{c} é de {a}m²')


print('Controle de Terrenos')
print('-' * 30)
l = float(input('Largura do terreno (m): '))
c = float(input('Comprimento do terreno (m): '))
area(l, c)
