# Ex028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverar escrever na tela se o usuário
# venceu ou perdeu.

from random import randint
from time import sleep
print('\033[1;33m-=-\033[m' * 20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente advinhar...\033[m')
print('\033[1;33m-=-\033[m' * 20)
n1 = randint(0, 5)  # Número do computador
n2 = int(input('Em que número pensei? '))  # Número do player
print('\033[35mPROCESSANDO...\033[m')
sleep(1.5)
print('o número que pensei foi \033[34m{}\033[m, o seu número foi \033[31m{}\033[m'.format(n1, n2))
if n1 == n2:
    print('\033[33mPARABÉNS! Você acertou o número!')
else:
    print('\033[31mQue pena! Você errou o número!')
