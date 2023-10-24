# Ex084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves

lista = []
aux_lista = []
maior = menor = 0

print('Cadastre nomes e pesos ')
while True:
    aux_lista.append(str(input('\nNome: ')))
    aux_lista.append(float(input('Peso: ')))
    lista.append(aux_lista[:])
    if aux_lista[1] > maior or len(lista) == 1:
        maior = aux_lista[1]
    if aux_lista[1] < menor or len(lista) == 1:
        menor = aux_lista[1]
    aux_lista.clear()
    while True:
        r = str(input('Deseja continuar [S/N]? ')).upper()
        if r in 'SN':
            break
    if r == 'N':
        break

print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'O maior peso foi {maior}Kg, peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi {menor}Kg, peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
