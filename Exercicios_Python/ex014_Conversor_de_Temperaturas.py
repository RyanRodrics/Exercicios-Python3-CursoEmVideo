# Ex014: Escreva um programa que leia uma temperatura digitada em °C e converta para °F.

C = float(input('Qual a temperatura em graus celcius? '))
F = 9 * C / 5 + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(C, F))
