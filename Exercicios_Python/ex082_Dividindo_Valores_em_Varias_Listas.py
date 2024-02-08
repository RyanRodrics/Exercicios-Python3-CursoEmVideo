# Ex082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        r = str(input('Deseja continuar [S/N]? ')).upper()
        if r in 'SN':
            break
    if r == 'N':
        break

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print('=-' * 30)
print('A lista completa é', lista)
print('A lista de pares é', pares)
print('A lista de impares é', impares)
