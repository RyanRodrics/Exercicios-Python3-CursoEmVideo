# Ex022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# --> O nome com todas as letras maiúsculas;
# --> O nome com todas as letras minúsculas;
# --> Quantas letras ao total (sem considerar espaços);
# --> Quantas letras tem o primeiro nome.

completo = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome..')
print('Seu nome em maiúsculas é', completo.upper())
print('Seu nome em minúsculas é', completo.lower())

nomes = completo.split()
letras = ''.join(nomes)

print('Seu nome completo tem {} letras'.format(len(letras)))
# print('Seu nome completo tem {} letras'.format(len(completo) - completo.count(' ')))

print('Seu primeiro nome tem {} letras'.format(len(nomes[0])))
# print('Seu primeiro nome tem {} letras'.format(completo.find(' ')))
