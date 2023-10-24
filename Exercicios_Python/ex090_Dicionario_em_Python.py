# Ex090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
# mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['status'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['status'] = 'Recuperação'
else:
    aluno['status'] = 'Reprovado'
print(f'{aluno["nome"]}, com média {aluno["media"]} está com status {aluno["status"]}')
