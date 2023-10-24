# Ex094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = list()
media = 0
while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper()
        if pessoa['sexo'] == 'M' or pessoa['sexo'] == 'F':
            break
        else:
            print('Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    while True:
        r = str(input('Deseja continuar [S/N]? ')).upper()
        if r in 'SN':
            print()
            break
        else:
            print('Digite apenas S ou N')
    if r == 'N':
        break
for p in pessoas:
    media += p['idade']
media = float(media) / len(pessoas)

print('-=' * 30)
print(f'-- O grupo tem {len(pessoas)} pessoas')
print(f'-- A media de idade é de {media} anos')
print('-- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print('\n-- Lista de pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\nENCERRADO')
