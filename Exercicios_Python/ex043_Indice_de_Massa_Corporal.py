# Ex043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# --> IMC abaixo de 18,5: Abaixo do Peso;
# --> Entre 18,5 e 25: Peso Ideal;
# --> 25 até 30: Sobrepeso;
# --> 30 até 40: Obesidade;
# --> Acima de 40: Obesidade Mórbida.

print('\033[34mVerifique seu IMC...\033[m')
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)
print('Seu IMC é \033[31m{:.1f}\033[m'.format(imc))
status = 'status'
if imc < 18.5:
    status = 'ABAIXO DO PESO'
elif 18.5 <= imc < 25:
    status = 'PESO IDEAL'
elif 25 <= imc < 30:
    status = 'SOBREPESO'
elif 30 <= imc < 40:
    status = 'OBESIDADE'
elif imc >= 40:
    status = 'OBESIDADE MÓRBIDA'
print('Seu status é \033[33m{}'.format(status))
