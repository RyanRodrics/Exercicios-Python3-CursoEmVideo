# Ex106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

def escreva(msg, cor=''):
    tam = len(msg) + 4
    print(cor, '~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print('\033[m')


def ajuda(cmd):
    escreva(f"Acessando manual de comando '{cmd}' ", cor='\033[0;30;42m')
    print('\033[0;30;43m')
    help(cmd)
    print('\033[m')


while True:
    escreva('SITEMA DE AJUDA PyHELP', cor='\033[0;30;44m')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

escreva('ATÉ LOGO!', cor='\033[0;30;41m')
