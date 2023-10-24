def moeda(valor=0):
    return f'R${valor:.2f}'.replace('.', ',')


def aumentar(valor=0, ajuste=0, format=False):
    valor += valor * ajuste / 100.0
    if format:
        return moeda(valor)
    else:
        return valor


def diminuir(valor=0, ajuste=0, format=False):
    valor -= valor * ajuste / 100.0
    if format:
        return moeda(valor)
    else:
        return valor


def dobro(valor=0, format=False):
    valor *= 2
    if format:
        return moeda(valor)
    else:
        return valor


def metade(valor=0, format=False):
    valor /= 2.0
    if format:
        return moeda(valor)
    else:
        return valor
