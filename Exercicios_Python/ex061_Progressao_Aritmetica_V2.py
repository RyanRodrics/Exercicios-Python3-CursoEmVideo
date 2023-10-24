# Ex061: Refaça o Ex051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

print('\033[33m=\033[m' * 25)
print('\033[36m{:^25}\033[m'.format('10 TERMOS DE UMA P.A'))
print('\033[33m=\033[m' * 25)

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 0

while c != 10:
    print(a1 + c * r, '-->', end=' ')
    c += 1
print('Acabou')
