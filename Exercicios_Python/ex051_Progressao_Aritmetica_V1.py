# Ex051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.

print('\033[33m=\033[m' * 25)
print('\033[36m{:^25}\033[m'.format('10 TERMOS DE UMA P.A'))
print('\033[33m=\033[m' * 25)

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = a1 + (10 - 1) * r

# Solução 1
print('\nSolução 1')
print('Os 10 primeiros termos da P.A de razão \033[31m{}\033[m e primeiro termo \033[34m{}\033[m são'.format(r, a1))
for c in range(a1, decimo + r, r):
    print(c, '-->', end=' ')
print('Acabou')

# Solução 2
print('\nSolução 2')
print('Os 10 primeiros termos da P.A de razão \033[31m{}\033[m e primeiro termo \033[34m{}\033[m são'.format(r, a1))
for c in range(0, 10):
    print(a1, '-->', end=' ')
    a1 += r
print('Acabou')

