# Ex031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

d = float(input('Qual a distância de sua viagem (km)? '))
# preço = d * 0.5 if d <= 200 else d * 0.45
if d <= 200:
    print('Sua passagem custará R${:.2f}'.format(d * 0.5))
else:
    print('Sua passagem custará R${:.2f}'.format(d * 0.45))
