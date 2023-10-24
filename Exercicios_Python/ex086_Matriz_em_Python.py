# Ex086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final,
# mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]

for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))

print('-=' * 30)
for i in range(3):
    for j in range(3):
        print(f'[ {matriz[i][j]} ]', end='')
    print()
