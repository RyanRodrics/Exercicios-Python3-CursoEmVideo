# Ex047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('Os número \033[36mpares\033[m entre \033[31m1 e 50\033[m são: ')
# for c in range(1, 51):
    # if c % 2 == 0:
        # print(c, end=' ')
for n in range(2, 51, 2):
    print(n, end=' ')
