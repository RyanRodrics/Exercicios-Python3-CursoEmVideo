# Ex045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
print('\033[33m-=-\033[m' * 20)
print('LET´S PLAY \033[1;36mJ O K E N P Ô\033[m')
print('\033[33m-=-\033[m' * 20)
print('Escolha sua jogada digitando o número correspondente...')

# OPÇÕES
itens = ('\033[31mPedra\033[m', '\033[34mPapel\033[m', '\033[33mTesoura\033[m')

# JOGADOR
player = int(input('\033[31mPedra(0)\033[m, \033[34mPapel(1)\033[m ou \033[33mTesoura(2)\033[m: '))
if player == 0 or player == 1 or player == 2:
    player = itens[player]
else:
    print('\033[31mERRO! Digite o número corretamente!\033[m')

# COMPUTADOR
pc = itens[randint(0, 2)]

print('\033[36mJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!\033[m')
sleep(0.5)
print('Computador jogou {}\nJogador jogou {}'.format(pc, player))

# EMPATE
if player == pc:
    print('\033[32mEMPATE\033[m')
# VITORIA DO PC
elif player == itens[0] and pc == itens[1] \
        or player == itens[1] and pc == itens[2] \
        or player == itens[2] and pc == itens[0]:
    print('VITÓRIA DO \033[32mCOMPUTADOR')
# VITORIA DO PLAYER
elif player == itens[0] and pc == itens[2] \
        or player == itens[1] and pc == itens[0] \
        or player == itens[2] and pc == itens[1]:
    print('VITÓRIA DO \033[32mJOGADOR')
