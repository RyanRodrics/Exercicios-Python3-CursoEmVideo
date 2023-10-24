# Ex037: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
# base de conversção.
# --> 1 para binário;
# --> 2 para octal;
# --> 3 para hexadecimal.

n = int(input('Digite um número inteiro: '))
# print('Ele pode ser convertido para \033[31mBinário(1)\033[m, \033[32mOctal(2)\033[m ou \033[34mHexadecimal(3)\033[m')
# x = int(input('Escolha a base de conversão de sua preferência digitando o dígito correspondente: '))
print('''Escolha uma das bases para conversão:
[1] Converter para \033[31mBinário\033[m
[2] Converter para \033[32mOctal\033[m
[3] Converter para \033[34mHexadecimal\033[m''')
x = int(input('Sua opção: '))
if x == 1:
    print(bin(n)[2:])
elif x == 2:
    print(oct(n)[2:])
elif x == 3:
    print(hex(n)[2:])
else:
    print('\033[31mERRO! Digite a opção corretamente!')
