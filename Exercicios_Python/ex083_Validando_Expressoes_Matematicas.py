# Ex083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
# analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite uma expressão: ')).strip()
parenteses = []

for c in expressao:
    if c in '()':
        parenteses.append(c)
# print(lista)

while len(parenteses) > 0:
    if parenteses[0] == ')' or parenteses[len(parenteses)-1] == '(':
        print('Essa expressão é Invalida')
        break
    elif ')' in parenteses:
        parenteses.remove('(')
        parenteses.remove(')')
        if len(parenteses) == 0:
            print('Essa expressão é válida')
