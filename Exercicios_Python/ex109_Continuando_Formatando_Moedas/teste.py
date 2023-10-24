# Ex109: Modifique as funções que foram criadas no Ex107 para que elas aceitem um parâmetro a mais, informando se
# o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no Ex108.

import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {p} é {moeda.metade(p, format=True)}')
print(f'O dobro de {p} é {moeda.dobro(p, format=True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, format=True)}')
print(f'Diminundo 13%, temos {moeda.diminuir(p, 13, format=True)}')
