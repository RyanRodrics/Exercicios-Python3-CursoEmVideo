# Ex053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA.

frase = input('Digite uma frase: ')
frase = frase.strip().upper().split()
frase = ''.join(frase)
inverso = ''
# inverso = frase[::-1]
for c in range(len(frase), 0, -1):
    inverso += frase[c - 1]
print('O inverso de {} é {}'.format(frase, inverso))
if frase == inverso:
    print('Você digitou um palíndromo KKKKKK')
else:
    print('Você não digitou um palíndromo')
