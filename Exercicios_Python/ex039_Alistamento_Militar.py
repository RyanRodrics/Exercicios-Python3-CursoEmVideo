# Ex039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# --> Se ele ainda vai se alistar;
# --> Se é a hora dele se alistar;
# --> Se já passou do tempo de alistamento.
# Seu proframa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
hoje = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
idade = hoje - nasc
print('Quem nasceu em {} completa {} anos em {}'.format(nasc, idade, hoje))
if idade == 18:
    print('Nesse ano você completa/completou 18 anos. \033[32mAliste-se já!')
elif idade > 18:
    d = idade - 18
    print('Seu alistamento foi em', nasc + 18)
    print('Passou \033[31m{}\033[m anos do tempo de alistamento'.format(d))
elif idade < 18:
    d = 18 - idade
    print('Seu alistamento será em', nasc + 18)
    print('Ainda não é hora de se alistar, falta \033[31m{}\033[m anos'.format(d))
