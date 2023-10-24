# Ex065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
# todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
# não continuar a digitar valores.

n = soma = c = maior = menor = 0
end = 'S'
while end == 'S':
    n = int(input('Digite um número inteiro: '))
    soma += n
    c += 1
    if c == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    end = str(input('Deseja continuar digitando [S/N]? ')).upper().strip()
    # if end != 'S' and end != 'N':
        # print('\033[31mOpção inválida, tente novamente\033[m')
    # break
print('Você digitou \033[31m{}\033[m números, cuja média foi \033[31m{:.2f}\033[m'.format(c, soma / c))
print('\033[31m{}\033[m foi o maior número digitado e \033[31m{}\033[m foi o menor'.format(maior, menor))
