# Ex087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[], [], []]
somaPar = 0
somaColum3 = 0

for i in range(3):
    for j in range(3):
        valor = int(input(f'Digite um valor para [{i}, {j}]: '))
        matriz[i].append(valor)
        if (valor % 2) == 0:
            somaPar += valor
        if j == 2:
            somaColum3 += valor

print('-=' * 30)
for i in range(3):
    for j in range(3):
        print(f'[ {matriz[i][j]} ]', end='')
    print()

# A)
print('Soma dos valores pares: ', somaPar)

# B)
print('Soma dos valores da terceira coluna: ', somaColum3)

# C)
print('Maior valor da segunda linha: ', sorted(matriz[1])[2])
