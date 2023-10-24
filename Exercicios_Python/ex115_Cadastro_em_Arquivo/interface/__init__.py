def cor(n):
    cores = [
        '\033[m',      # sem cor
        '\033[0;31m',  # vermelho
        '\033[0;32m',  # verde
        '\033[0;33m',  # amarelo
        '\033[0;34m',  # azul
        '\033[0;35m',  # roxo
        '\033[0;36m',  # ciano
    ]
    return cores[n]


def linha(tam=50):
    return '-' * tam


def head(txt, tam=50):
    print(linha(tam))
    print(txt.center(tam))
    print(linha(tam))


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'{cor(1)}ERRO! Por favor digite um número inteiro válido{cor(0)}')
        except KeyboardInterrupt:
            print(f'\n{cor(1)}Entrada de dados interrompida pelo usuário.{cor(0)}')
            return 0
        else:
            return n


def menu(lista):
    head('MENU PRINCIPAL')
    for i, elem in enumerate(lista):
        print(f'{cor(3)}[{i+1}]{cor(0)} {cor(4)}{elem}{cor(0)}')
    print(linha())
    while True:
        op = leiaInt(f'{cor(2)}Sua opção:{cor(0)} ')
        if op <= 0 or op > len(lista):
            print(f'{cor(1)}Opção Inválida. Tente Novamente.{cor(0)}')
        else:
            break
    return op
