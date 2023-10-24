# Ex036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa, o salário do comprador
# e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
# salário ou então não é negado.

print('\033[35mInsira os dados para a aprovação do seu empréstimo:\033[m')
c = float(input('Valor da casa: R$'))
s = float(input('Salário: R$'))
t = int(input('Anos que pretende pagar: '))
mensal = c / (t * 12)
print('Você terá que pagar \033[31mR${:.2f}\033[m mensalmente por \033[34m{}\033[m anos'.format(mensal, t))
if mensal >= s * 0.3:
    print('Seu empréstimo foi \033[1;31mNEGADO')
else:
    print('Seu empréstimo foi \033[1;32mAPROVADO')
