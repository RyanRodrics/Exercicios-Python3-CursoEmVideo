# Ex006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
# r = n ** (1 / 2)
r = pow(n, (1 / 2))
print('O dobro de {} é {}, o triplo é {}, e a raiz quadrada é {:.3f}'.format(n, d, t, r))
print('Dobro: {} \nTriplo: {} \nRaiz: {:.3f}'.format(d, t, r))
