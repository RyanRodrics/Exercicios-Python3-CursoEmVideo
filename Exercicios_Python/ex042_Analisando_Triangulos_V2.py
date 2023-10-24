# Ex042: Refaça o Ex035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# --> Equilátero: todos os lados iguais;
# --> Isósceles: dois lados iguais;
# --> Escaleno: todos os lados diferente.

print('\033[1;33m-=-\033[m' * 20)
print('\033[34mANALISANDO TRIÂNGULOS...\033[m')
print('\033[1;33m-=-\033[m' * 20)
print('Digite o comprimento de 3 segumentos (na mesma grandeza)')
r1 = float(input('Seguimento 1: '))
r2 = float(input('Seguimento 2: '))
r3 = float(input('Seguimento 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos satisfazem a condição de existência e conseguem formar um triângulo')
    print('O triângulo formado é ', end='')
    if r1 == r2 == r3:
        print('\033[32mEQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('\033[32mISÓCELES')
    elif r1 != r2 != r3:
        print('\033[32mESCALENO')
else:
    print('Os seguimentos não satisfazem a condição de existência e não conseguem formar um triâgulo')
