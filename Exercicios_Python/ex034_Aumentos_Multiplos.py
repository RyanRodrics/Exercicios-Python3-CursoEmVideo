# Ex034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para valores superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Digite seu salário: R$'))
if s > 1250:
    print('Você receberá um aumento de R${:.2f}'.format(s * 0.1))
else:
    print('Você receberá um aumento de R${:.2f}'.format(s * 0.15))
