# Ex068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print('\033[33m-\033[m' * 25)
print('\033[36mLET´S PLAY IMPAR OU PAR\033[m')
print('\033[33m-\033[m' * 25)
v = 0

while True:
    # Jogador
    playernum = int(input('Qual número vai jogar [0 a 10]? '))
    player = str(input('Par ou Ímpar [P/I]? ')).upper().strip()

    # Computador
    pcnum = randint(0, 10)
    if player == 'P':
        pc = 'I'
    elif player == 'I':
        pc = 'P'

    # Play Time
    soma = playernum + pcnum
    if soma % 2 == 0:
        pi = str('PAR')
    else:
        pi = str('ÍMPAR')
    print(f'Você jogou {playernum} e o computador jogou {pcnum}. Total de {soma}, \033[36m{pi}\033[m')

    if (player == 'P' and pi == 'PAR') or (player == 'I' and pi == 'ÍMPAR'):
        print('\033[32mVocê VENCEU! Vamos jogar novamente...\033[m\n')
        v += 1
    else:
        break
print(f'\n\033[31mGAME OVER!\033[33m Você teve {v} vitórias consecutivas')
