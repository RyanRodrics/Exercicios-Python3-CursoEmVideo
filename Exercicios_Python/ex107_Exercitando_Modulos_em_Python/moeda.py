def aumentar(valor, ajuste):
    valor += valor * ajuste / 100.0
    return valor


def diminuir(valor, ajuste):
    valor -= valor * ajuste / 100.0
    return valor


def dobro(valor):
    valor *= 2
    return valor


def metade(valor):
    valor /= 2.0
    return valor
