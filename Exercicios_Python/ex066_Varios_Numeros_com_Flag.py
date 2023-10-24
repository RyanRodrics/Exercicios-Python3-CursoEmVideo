# Ex066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
# elas (desconsiderando o flag).

n = c = s = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Você digitou {c} números, cuja soma foi {s}')
