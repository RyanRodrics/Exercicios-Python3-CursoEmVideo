# Ex100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
# soma entre todos os valores pares sorteados pela função anterior.

from random import randint


def sorteia(lst):
    print('Sorteando valores: ', end='')
    for i in range(5):
        lst.append(randint(1, 10))
        print(lst[i], end=' ')
    print()


def somapar(lst):
    print(f'Soma dos valores pares de {lst}: ', end='')
    soma = 0
    for num in lst:
        if num % 2 == 0:
            soma += num
    print(soma)


numeros = list()
sorteia(numeros)
somapar(numeros)
