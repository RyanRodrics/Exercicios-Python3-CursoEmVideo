# Ex015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60,00 por dia e R$0,15 por Km rodado.

d = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km rodados? '))
# R$60.00 por dia e R$0.15 por km rodado
# t = d * 60 + km * 0.15
print('o total a pagar é de R${:.2f}'.format(d * 60 + km * 0.15))
