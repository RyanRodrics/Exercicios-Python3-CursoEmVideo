# Ex099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(*valores):
    m = 0
    print('-=' * 20)
    print('Analisando os valores...')
    sleep(0.5)
    for i in valores:
        print(i, end=' ')
        if i > m:
            m = i
    print(f'Foram informados {len(valores)} valores')
    print(f'O maior valor informado foi {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
