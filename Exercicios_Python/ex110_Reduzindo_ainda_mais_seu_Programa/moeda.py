def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


def aumentar(valor, ajuste, format=False):
    valor += valor * ajuste / 100.0
    if format:
        return moeda(valor)
    else:
        return valor


def diminuir(valor, ajuste, format=False):
    valor -= valor * ajuste / 100.0
    if format:
        return moeda(valor)
    else:
        return valor


def dobro(valor, format=False):
    valor *= 2
    if format:
        return moeda(valor)
    else:
        return valor


def metade(valor, format=False):
    valor /= 2.0
    if format:
        return moeda(valor)
    else:
        return valor


def resumo(valor, aumento, reducao):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}', moeda(valor))
    print(f'{"Dobro do preço":<20}', dobro(valor, format=True))
    print(f'{"Metade do preço:":<20}', metade(valor, format=True))
    print(f'{f"{aumento}% de aumento:":<20}', aumentar(valor, aumento, format=True))
    print(f'{f"{reducao}% de redução:":<20}', diminuir(valor, reducao, format=True))
    print('-' * 30)
