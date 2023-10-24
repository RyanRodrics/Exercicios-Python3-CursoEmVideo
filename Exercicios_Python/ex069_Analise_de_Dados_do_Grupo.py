# Ex069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maiores = homens = jovens = 0

while True:
    print('-' * 30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('-' * 30)

    sexo = ' '
    stop = ' '
    idade = int(input('Idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        if idade < 20:
            jovens += 1
    while stop not in 'SN':
        stop = str(input('Quer continuar [S/N]? ')).upper().strip()
    print(' ')
    if stop == 'N':
        break

print(f'Foram cadastradas {maiores} pessoas maiores de idade')
print(f'Foram cadastrados {homens} homens')
print(f'Foram cadastradas {jovens} mulheres menores de 20 anos')
