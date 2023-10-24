# Ex030: Crie um programa que leia um número inteiro e mostre na tela se ele é Par ou Ímpar.

n = int(input('Digite um número inteiro: '))
if n % 2 == 0:
    print('O número \033[31m{}\033[m é \033[1;36mPAR'.format(n))
else:
    print('O número \033[31m{}\033[m é \033[1;36mÍMPAR'.format(n))
