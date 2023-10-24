# Ex017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

import math
c1 = float(input('Qual o comprimento de um cateto? '))
c2 = float(input('Qual o comprimento do outro cateto? '))
# hi = math.sqrt(pow(c1, 2) + pow(c2, 2))
hi = math.hypot(c1, c2)
print('A hipotenuza desse triângulo retângulo mede: ', hi)
