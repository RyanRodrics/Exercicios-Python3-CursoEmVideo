# Ex075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

print("Digite 4 valores inteiros:")
tupla = (int(input("N1: ")),
         int(input("N1: ")),
         int(input("N1: ")),
         int(input("N1: ")))
#cont = 0
print("Você digitou os valores: ", tupla)

#A
#for numero in tupla:
#    if numero == 9:
#        cont += 1
print(f"O valor 9 aparece {tupla.count(9)} vezes")

#B
cont = 0
#for i, elemento in enumerate(tupla):
#    if elemento == 3:
#        cont = i + 1
#        break
#if cont != 0:
if 3 in tupla:
    print("O primeiro valor 3 apareceu na posição ", tupla.index(3))
else:
    print("O valor 3 não apareceu")

#C
print("Números pares: ", end='')
for numero in tupla:
    if numero % 2 == 0:
        print(f"{numero} ", end='')
