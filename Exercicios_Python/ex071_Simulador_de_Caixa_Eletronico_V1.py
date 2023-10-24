# Ex071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
# o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 30)
print(f'{"BANCO RODRIGUES":^30}')
print('=' * 30)

valor = int(input('Quanto deseja sacar? R$'))
cem = cinquenta = vinte = dez = cinco = dois = um = 0
print('Total de: ')

if valor >= 100:
    cem = valor // 100
    valor %= 100
    print(f'{cem} notas de R$100.00')
if valor >= 50:
    cinquenta = valor // 50
    valor %= 50
    print(f'{cinquenta} notas de R$50.00')
if valor >= 20:
    vinte = valor // 20
    valor %= 20
    print(f'{vinte} notas de R$20.00')
if valor >= 10:
    dez = valor // 10
    valor %= 10
    print(f'{dez} notas de R$10.00')
if valor >= 5:
    cinco = valor // 5
    valor %= 5
    print(f'{cinco} notas de R$5.00')
if valor >= 2:
    dois = valor // 2
    valor %= 2
    print(f'{dois} notas de R$2.00')
if valor == 1:
    print('1 moeda de R$1,00')
print('=' * 30)
print('Volte sempre no BANCO RODRIGUES! Tenha um bom dia!')
