# Ex071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
# o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 30)
print(f'{"BANCO RODRIGUES":^30}')
print('=' * 30)

valor = int(input('Quanto deseja sacar? R$'))
cedula = 100
cedulanum = 0
print('Total de: ')

while True:
    if valor >= cedula:
        valor -= cedula
        cedulanum += 1
    else:
        if cedulanum > 0:
            print(f'{cedulanum} cédulas de R${cedula:.2f}')
        if valor == 1:
            print('1 moeda de R$1.00')
            valor = 0
        if cedula == 100:
            cedula = 50
            cedulanum = 0
        elif cedula == 50:
            cedula = 20
            cedulanum = 0
        elif cedula == 20:
            cedula = 10
            cedulanum = 0
        elif cedula == 10:
            cedula = 5
            cedulanum = 0
        elif cedula == 5:
            cedula = 2
            cedulanum = 0
        elif cedula == 2:
            cedula = 1
            cedulanum = 0
        if valor == 0:
            break

print('=' * 30)
print('Volte sempre no BANCO RODRIGUES! Tenha um bom dia!')
