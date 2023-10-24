# Ex049: Refaça o Ex009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número inteiro para ver sua tabuada: '))
print('\033[33m_\033[m' * 13)
for c in range(1, 11):
    print('{}  X {:>2} = \033[34m{:>2}\033[m'.format(n, c, n * c))
print('\033[33m_\033[m' * 13)
