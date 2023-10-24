# Ex081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        r = str(input('Deseja continuar [S/N]? ')).upper()
        if r in 'SN':
            break
    if r == 'N':
        break
print('=-' * 30)

#A)
print(f'Você digitou {len(lista)} elementos')

#B)
lista.sort(reverse=True)
print('O valores em ordem decrescente são', lista)

#C)
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
