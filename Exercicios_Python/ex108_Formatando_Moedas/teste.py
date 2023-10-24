# Ex108: Adapte o código do Ex107, criando uma função adicional chamada moeda() que consiga mostrar os números
# como um valor monetário formatado.

import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {p} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {p} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminundo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')
