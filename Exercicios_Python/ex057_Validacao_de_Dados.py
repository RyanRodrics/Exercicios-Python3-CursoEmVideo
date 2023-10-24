# Ex057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

sexo = ' '
while sexo not in 'MF':
    sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()
    if sexo not in 'MF':
        print('\033[31mResposta inválida! Tente novamente\033[m')
print('\033[32mSexo {} registrado com sucesso'.format(sexo))
