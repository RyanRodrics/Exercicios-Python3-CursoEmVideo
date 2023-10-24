# Ex025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual é o seu nome? ')).strip()
print('Você tem Silva no nome?', 'SILVA' in nome.upper())
