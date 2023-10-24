# Ex080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na
# posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = []
aux = 0

for i in range(5):
    aux = int(input('Digite um valor: '))
    #valores.append(aux)
    #valores.insert(sorted(valores).index(aux), aux)
    #valores.pop()
    #if valores.index(aux) == len(valores)-1:
    #    print('Adicionado ao final da lista')
    #else:
    #    print(f'Adicionado na posição {valores.index(aux)} da lista...')
    if i == 0 or aux > valores[len(valores)-1]:
        valores.append(aux)
        print('Adicionado ao final da lista...')
    else:
        for pos in range(len(valores)):
            if aux <= valores[pos]:
                valores.insert(pos, aux)
                print(f'Adicionado na posição {pos} da lista...')
                break

print('=-' * 30)
print('Os valores digitados em ordem foram', valores)
