# Ex095: Aprimore o Ex093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador.

time = list()
jogador = dict()
gols = list()
while True:
    print('-' * 40)
    total = 0
    jogador['nome'] = str(input('Nome do Jogador: '))
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(n):
        gols_partida = int(input(f'Quantos gols na partida {i+1}? '))
        total += gols_partida
        gols.append(gols_partida)
    jogador['gols'] = gols[:]
    gols.clear()
    jogador['total'] = total
    time.append(jogador.copy())
    while True:
        r = str(input('Deseja continuar [S/N]? ')).upper()
        if r in 'SN':
            print()
            break
    if r == 'N':
        break

print('-=' * 30)
print('N° ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k+1:}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    cod = int(input('Deseja acessar qual jogador (999 para sair)? '))
    if cod == 999:
        break
    if cod > len(time) or cod <= 0:
        print('Esse jogador não existe. Tente novamente')
        continue
    print(f'O jogador {time[cod-1]["nome"]} jogou {n} partidas')
    for i, j in enumerate(time[cod-1]['gols']):
        print(f'Na partida {i + 1}, fez {j} gols.')
    print(f'Foi um total de {time[cod-1]["total"]} gols')
    while True:
        r = str(input('Deseja continuar [S/N]? ')).upper()
        if r in 'SN':
            print()
            break
    if r == 'N':
        break
print('ENCERRADO')
