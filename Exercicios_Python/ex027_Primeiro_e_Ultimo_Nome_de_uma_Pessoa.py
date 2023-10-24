# Ex027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e
# o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu primeiro nome é', nome.split()[0])
ultimo = len(nome.split()) - 1
print('Seu ultimo nome é', nome.split()[ultimo])
