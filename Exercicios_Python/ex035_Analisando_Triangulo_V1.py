# Ex035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo.

print('-=-' * 20)
print('ANALISANDO TRIÂNGULOS...')
print('-=-' * 20)
print('Digite o comprimento de 3 seguimentos (na mesma grandeza): ')
r1 = float(input('Seguimento 1: '))
r2 = float(input('Seguimento 2: '))
r3 = float(input('Seguimento 3: '))
if r2 + r3 > r1 > abs(r2 - r3) or r1 + r3 > r2 > abs(r1 - r3) or r1 + r2 > r3 > abs(r1 + r2):
# if  r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2
    print('Os seguimentos conseguem formar um triângulo')
else:
    print('Os seguimentos não conseguem formar um triângulo')
