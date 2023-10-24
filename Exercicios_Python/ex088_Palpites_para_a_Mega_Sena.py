# Ex088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
jogos = []
aux_jogo = []

print('-' * 35)
print(f'{"JOGA NA MEGA SENA":^35}')
print('-' * 35)
n = int(input('Quantos jogos você quer sortear? '))

print(f'\n{f"SORTEANDO {n} JOGOS":*^35}')
for i in range(n):
    print(f'Jogo {i+1}: ', end='')
    for j in range(6):
        while True:
            num = randint(1, 60)
            if num not in aux_jogo:
                aux_jogo.append(num)
                break
    jogos.append(sorted(aux_jogo))
    print(jogos[i])
    aux_jogo.clear()
print('-='*5, '< BOA SORTE! >', '-='*5)
