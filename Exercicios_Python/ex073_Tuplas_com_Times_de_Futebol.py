# Ex073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Cruzeiro.

times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fluminense', 'Grêmio',
         'Athletico-PR', 'Bragantino', 'Fortaleza', 'Cuiaba', 'São Paulo',
         'Alético-MG', 'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás',
         'Bahia', 'Santos', 'Vasco da Gama', 'Coritiba', 'América-MG')
print('Lista de times: ', times)

# A)
print('\nA) ')
for ordem, primeiros in enumerate(times[0:5]):
    print(f'{ordem + 1}º - {primeiros}',)

#B)
print('\nB) ')
for ordem, ultimos in enumerate(times[-4:]):
    print(f'{ordem + 17}º - {ultimos}')

#C)
print('\nC) ')
print(sorted(times))

#D)
print('\nD) ')
#for ordem, time in enumerate(times):
#    if time == 'Cruzeiro':
#        print(f'Cruzeiro esta na {ordem + 1}º posição ')
print(f'O Cruzeiro está na posição {times.index("Cruzeiro") + 1}')
