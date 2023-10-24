# Ex070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('\033[33m-\033[m' * 35)
print(f'\033[36m{"LOJAS RODRIGUES":^35}\033[m')
print('\033[33m-\033[m' * 35)
total = caros = menor = c = 0
barato = ' '

while True:
    stop = ' '
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço: R$'))
    c += 1
    total += valor
    if valor > 1000:
        caros += 1
    if c == 1:
        menor = valor
    if valor < menor:
        menor = valor
        barato = str(nome)

    while stop not in 'NS':
        stop = str(input('Quer continuar [S/N]?')).upper().strip()[0]
    print(' ')
    if stop == 'N':
        break

print(f'\033[31m{" FIM DO PROGRAMA ":-^35}\033[m')
print(f'Total de \033[32m{c}\033[m produtos')
print(f'O total da compra foi de \033[32mR${total:.2f}\033[m')
print(f'Temos \033[35m{caros}\033[m produtos custando mais de R$1000.00')
print(f'O produto mais barato foi \033[34m{barato}\033[m, custando \033[34mR${menor:.2f}')
