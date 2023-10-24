# Ex078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior
# e o menor valor digitado e as suas respectivas posições na lista.

lista = []
#index_maior = []
#index_menor = []

for i in range(5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
maior = sorted(lista)[len(lista)-1]
menor = sorted(lista)[0]
#for index, valor in enumerate(lista):
#    if maior == valor:
#        index_maior.append(index)
#    if menor == valor:
#        index_menor.append(index)

print('=-' * 30)
print('Você digitou os valores: ', lista)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for index, valor in enumerate(lista):
    if valor == maior:
        print(f'...{index} ', end='')
print(f'\nO menor valor digitados foi {menor} nas posições ', end='')
for index, valor in enumerate(lista):
    if valor == menor:
        print(f'...{index} ', end='')
