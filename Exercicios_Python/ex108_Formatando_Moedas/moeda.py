def aumentar(valor=0, ajuste=0):
    valor += valor * ajuste / 100.0
    return valor


def diminuir(valor=0, ajuste=0):
    valor -= valor * ajuste / 100.0
    return valor


def dobro(valor=0):
    valor *= 2
    return valor


def metade(valor=0):
    valor /= 2.0
    return valor


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
