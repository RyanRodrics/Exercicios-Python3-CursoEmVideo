# Ex040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# --> Média abaixo de 5.0: REPROVADO.
# --> Média entre 5.0 e 6.9: RECUPERAÇÃO.
# --> Média 7.0 ou superior: APROVADO.


print('Digite abaixo suas notas')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Sua média foi \033[31m{:.1f}\033[m. Você foi \033[31mREPROVADO.'.format(m))
elif 7 > m >= 5:
    print('Sua média foi \033[31m{:.1f}\033[m. Você está de \033[33mRECUPERAÇÃO.'.format(m))
elif m >= 7:
    print('Sua média foi \033[31m{:.1f}\033[m. PARABÉNS! Você foi \033[32mAPROVADO!'.format(m))
