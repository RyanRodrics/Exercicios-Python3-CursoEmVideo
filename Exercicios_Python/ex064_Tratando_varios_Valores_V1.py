# Ex064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a
# soma entre eles (desconsiderando o flag).

s = end = c = 0
while end != 999:
    end = int(input('Digite para somar [999 se quiser encerrar]: '))
    s += end
    c += 1
print('A soma {} dos números digitados foi {}'.format(c - 1, s - 999))
