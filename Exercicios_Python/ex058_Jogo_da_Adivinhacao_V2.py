# Ex058: Melhore o jogo do Ex028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
print('\033[1;33m-=-\033[m' * 20)
print('\033[36mVou pensar em um número entre 0 e 10. Tente advinhar...\033[m')
print('\033[1;33m-=-\033[m' * 20)

pc = randint(0, 10)
player = 11
palpites = 0
acertou = False

while not acertou:
    player = int(input('Em que número pensei? '))
    if pc > player:
        print('\033[31mMais... Tente novamente...\033[m')
    elif pc < player:
        print('\033[31mMenos... Tente novamente\033[m')
    else:
        acertou = True
        print('\033[32mParabéns! Você acertou o número!\033[m')
    palpites += 1
print('Você precisou de \033[34m{}\033[m tentativas'.format(palpites))
