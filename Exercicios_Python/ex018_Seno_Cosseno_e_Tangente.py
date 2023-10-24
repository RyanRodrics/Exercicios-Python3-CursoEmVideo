# Ex018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
a = int(input('Digite um ândulo do círculo trigonométrico(em graus): '))
sin = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('SENO: {:.2f}\nCOSSENO: {:.2f}\nTANGENTE: {:.2f}'.format(sin, cos, tan))
