# Ex041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:
# --> Até 9 anos: MIRIM;
# --> Até 14 anos: INFANTIL;
# --> Até 19 anos: JUNIOR;
# --> Até 25 anos: SÊNIOR;
# --> Acima: MASTER;

from datetime import date
print('\033[34mConfira sua categoria de competição da CNN\033[m')
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
verde = '\033[32m'
violeta = '\033[35m'
limpa = '\033[m'
print('O atleta tem {}{}{} anos '.format(violeta, idade, limpa))
if idade <= 9:
    print('Sua categoria é {}MIRIM{}'.format(verde, limpa))
elif idade <= 14:
    print('Sua categoria é {}INFANTIL{}'.format(verde, limpa))
elif idade <= 19:
    print('Sua categoria é {}JÚNIOR{}'.format(verde, limpa))
elif idade <= 25:
    print('Sua categoria é {}SÊNIOR{}'.format(verde, limpa))
elif idade > 20:
    print('Sua categoria é {}MASTER{}'.format(verde, limpa))
