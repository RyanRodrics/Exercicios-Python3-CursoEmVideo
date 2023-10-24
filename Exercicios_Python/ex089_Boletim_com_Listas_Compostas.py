# Ex089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

lista = []
alunos = []
notas = []

print('Registre alunos')
while True:
    alunos.append(str(input('\nNome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 1: ')))
    alunos.append(notas[:])
    alunos.append((notas[0]+notas[1]) / 2.0)
    lista.append(alunos[:])
    notas.clear()
    alunos.clear()
    while True:
        r = str(input('Deseja continuar [S/N]? ')).upper()
        if r in 'SN':
            break
    if r == 'N':
        break

print('-=' * 15)
print(f'{"N°":<10} {"NOME":<10} {"MÉDIA":<10}')
print('-' * 30)
for i, aluno in enumerate(lista):
    print(f'{i+1:<10}', f'{aluno[0]:<10}', f'{aluno[2]:<10.2f}')
print('-=' * 15)

while True:
    pos = int(input('\nDeseja acessar as notas de qual aluno (999 para sair)? ')) - 1
    if pos == 998:
        break
    print(f'Notas de {lista[pos][0]}: ', lista[pos][1])
