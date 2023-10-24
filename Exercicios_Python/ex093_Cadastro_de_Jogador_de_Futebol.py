# Ex093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Nome do Jogador: '))
n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(n):
    gols_partida = int(input(f'Quantos gols na partida {i+1}? '))
    total += gols_partida
    gols.append(gols_partida)
jogador['gols'] = gols[:]
jogador['total'] = total

print('\n', '-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {n} partidas')
for i, j in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {j} gols.')
print(f'Foi um total de {jogador["total"]} gols')
