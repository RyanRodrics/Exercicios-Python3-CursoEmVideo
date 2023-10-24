# Ex56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de
# idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

nome = ''
idades = 0
media = 0
nomevelho = 'nenhum'
idadevelho = 0
sexo = ''
mulherjovem = 0

print('Preencha os campos abaixo com o nome, idade e sexo de 5 pessoas, para fins de pesquisa')

for p in range(1, 5):

    # lendo nome, idade e sexo
    print('---------- {}ª PESSOA ----------'.format(p))
    nome = str(input('Nome: '))
    idades = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))

    # contador somando idades
    media += idades

    # verificando se é o mais velho e salvando nome e idade
    if sexo in 'Mn' and idades > idadevelho:
        nomevelho = nome
        idadevelho = idades

    # contador mulheres jovens
    if sexo in 'Ff' and idades < 20:
        mulherjovem += 1

print('\nA média das idades digitadas é {} anos'.format(media / 4))
if nomevelho == 'nenhum':
    print('Nenhum homem participou da pesquisa')
else:
    print('O homem mais velho tem {} anos e se chama {}'.format(idadevelho, nomevelho))
print('Das mulheres apresentadas, {} são menores de 20 anos'.format(mulherjovem))
