# Ex029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

V = float(input('Qual a velocidade do carro (km/h) ? '))
multa = (V - 80) * 7
if V > 80:
    print('\033[31mMULTADO! Você está acima do limite de velocidade que é 80 km/h')
    print('Sua multa é de \033[1;33mR${:.2f}'.format(multa))
else:
    print('\033[32mVocê está dentro do limite de velocidade\nTenha um bom dia e dirija com segurança')
