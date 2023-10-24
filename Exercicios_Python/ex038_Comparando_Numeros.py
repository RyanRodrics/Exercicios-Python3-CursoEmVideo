# Ex038: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# --> "O primeiro valor é o maior."
# --> "O segundo valor é o maior."
# --> "Os valores são iguais."

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O \033[31mprimeiro\033[m valor é maior')
elif n2 > n1:
    print('O \033[31msegundo\033[m valor é maior')
elif n1 == n2:
    print('Os valores são \033[31miguais')
    