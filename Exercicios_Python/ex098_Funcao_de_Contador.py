# Ex098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    cont = inicio
    if passo < 0:
        passo *= -1
    if passo == 0:
        print('ERRO. Não é possível avançar de 0 em 0.')
    elif inicio < fim:
        while cont <= fim:
            print(f'{cont} --> ', end='')
            sleep(0.5)
            cont += passo
    elif inicio > fim:
        while cont >= fim:
            print(f'{cont} --> ', end='')
            sleep(0.5)
            cont -= passo
    print('FIM')


# A)
print('A) ', end='')
contador(1, 10, 1)

# B)
print('\nB) ', end='')
contador(10, 0, 2)

# C)
print('\nC)')
print('Agora é sua vez de personalizar a contagem')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
