# Ex044:  Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
# --> à vista dinheiro/cheque: 10% de desconto;
# --> à vista no cartão: 5% de desconto;
# --> em até 2x no cartão: preço formal;
# --> 3x ou mais no cartão: 20% de juros.

# cores = {'limpa': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m'}
print('\033[36m{}{}{}\033[m'.format('=' * 20, ' LOJAS RODRIGUES ', '=' * 20))
p = float(input('Preço das compras: R$'))
print('''Escolha a forma de pagamento...
\033[35m[1] Dinheiro (à vista)\033[m
\033[33m[2] Cheque (à vista)\033[m
\033[34m[3] Cartão\033[m ''')
# f = int(input('Digite 1 para \033[33mDINHEIRO\033[m, 2 para \033[35mCHEQUE\033[m e 3 para \033[34mCARTÃO\033[m: '))
f = int(input('Sua opção: '))
if f == 1 or f == 2:
    print('O valor das compras de \033[31mR${:.2f}\033[m tem \033[36m10%\033[m de desconto e '
          'sai por \033[31mR${:.2f}\033[m'.format(p, p * 0.9))
elif f == 3:
    x = int(input('Em quantas vezes deseja parcelar (digite 1 se for à vista): '))
    if x == 1:
        print('O valor das compras de \033[31mR${:.2f}\033[m tem \033[36m5%\033[m de desconto e '
              'sai por \033[31mR${:.2f}\033[m'.format(p, p * 0.95))
    elif x == 2:
        print('O valor das compras custará seu preço normal de \033[31mR${:.2f}\033[m'.format(p))
        print('Serão duas parcelas mensais de \033[31mR${:.2f}\033[m'.format(p / 2))
    else:
        print('O valor das compras de \033[31mR${:.2f}\033[m terá \033[33m20%\033[m de juros e '
              'sairá por \033[31mR${:.2f}\033[m'.format(p, p * 1.2))
        print('Serão {} parcelas mensais de \033[31mR${:.2f}\033[m'.format(x, p * 1.2 / x))
else:
    print('\033[31mOpção inválida! Tente novamente!\033[m')
