# Ex013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Qual o seu salário: '))
a = s * 1.15
print('Seu salário, com 15% de aumento, fica R${:.2f}'.format(a))
