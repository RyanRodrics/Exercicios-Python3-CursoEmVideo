# Ex008: Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

m = float(input('Digite um valor em metros: '))
# cm = m * 100
# mm = m * 1000
# print('Centímetros: {} \nMilímetros: {}'.format(c, mm))
print('A medida de {}m corresponde a: '.format(m))
print('{} km\n{} hm\n{} dam\n{} dm\n{} cm\n{} mm'.format(m / 1000, m / 100, m / 10, m * 10, m * 100, m * 1000,))
