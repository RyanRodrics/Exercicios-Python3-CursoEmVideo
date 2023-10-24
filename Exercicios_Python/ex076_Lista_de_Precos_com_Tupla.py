# Ex076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.20,
          'Compasso', 9.9, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)

for i, produto in enumerate(listagem):
    if i % 2 == 0:
        print(f"{produto:.<20}R${listagem[i+1]:>7.2f}")
print('-' * 30)
