# Ex103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de
# um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
# dado não tenha sido informado corretamente.

def ficha(j='<desconhecido>', g=0):
    return f'Jogador {j} fez {g} gol(s)'


nome = str(input('Nome do Jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    print(ficha(g=gols))
else:
    print(ficha(nome, gols))
