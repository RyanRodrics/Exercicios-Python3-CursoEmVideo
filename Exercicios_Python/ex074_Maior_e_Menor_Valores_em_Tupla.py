# Ex074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

sorteados = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

print('OS valores sorteados foram:', sorteados)
#print("O maior valor sorteado foi: ", sorted(sorteados)[len(sorteados)-1])
#print("O menor valor sorteado foi: ", sorted(sorteados)[0])
print('O maior valor sorteado foi:', max(sorteados))
print('Om menor valor sorteado foi:', min(sorteados))
