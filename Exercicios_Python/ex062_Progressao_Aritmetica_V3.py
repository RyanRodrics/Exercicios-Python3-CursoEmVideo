# Ex062: Melhore o Ex061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('\033[33m=\033[m' * 25)
print('\033[36m{:^25}\033[m'.format('N TERMOS DE UMA P.A'))
print('\033[33m=\033[m' * 25)

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
n = int(input('Quantos termos? '))
c = 0
end = 1

while end != 0:
    while c < n:
        print(a1 + c * r, '-->', end=' ')
        c += 1
    if n != 0:
        end = int(input('\nDeseja ver mais quantos termos? '))
        n += end
print('FIM')
print('Progressão finalizada com {} termos mostrados'.format(n))
