# Ex012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o preço do produto: R$'))
d = p * 0.95
print('O produto custa R${:.2f} com 5% de desconto'.format(d))
