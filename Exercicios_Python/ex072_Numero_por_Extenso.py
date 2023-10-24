# Ex072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez'
           , 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        n = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= n <= 20:
            print(f'O numero {n} escrito por extenso é \033[31m{numeros[n]}\033[m')
            break
        print('Tente novamente. ', end='')
    while True:
        r = str(input('Deseja continuar [S/N]? ')).upper()
        if r == 'S' or r == 'N':
            print(' ')
            break
    if r == 'N':
        break
