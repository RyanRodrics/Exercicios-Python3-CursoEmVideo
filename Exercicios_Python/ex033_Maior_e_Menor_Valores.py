# Ex033: Faça um programa que leia 3 números e mostre qual o menor e qual o menor.

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um segundo valor: '))
n3 = float(input('Digite um terceiro valor: '))

# Verificando o maior
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

# Verificando o menor
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

if n1 == n2 == n3:
    print('Os valores são iguais bro')
else:
    print('{} é o maior valor e {} é o menor valor'.format(maior, menor))
