# Ex092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em
# um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação
# e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - nascimento
pessoa['ctps'] = int(input('N° carteira de trabalho (0 se não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['aposentadoria'] = pessoa['contratação'] + 35 - nascimento
    pessoa['salario'] = float(input('Salário: '))

print('-=' * 30)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
    