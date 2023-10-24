# Ex104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input()
# do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Exemplo: n = leiaInt('Digite um n: ')

def leiaint(frase):
    while True:
        num = input(frase)
        if num.isnumeric():
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return num


n = leiaint('Digite um número inteiro: ')
print(f'\nVocê acabou de digitar o número {n}')
