# Ex085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], []]

for i in range(7):
    n = int(input(f'Digite o {i+1}º valor inteiro: '))
    if (n % 2) == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

print('Valores pares digitados: ', sorted(valores[0]))
print('Valores impares digitados: ', sorted(valores[1]))
