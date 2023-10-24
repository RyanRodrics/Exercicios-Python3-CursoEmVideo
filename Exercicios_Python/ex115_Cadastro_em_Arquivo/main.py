# Ex115: Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo nome e idade em um arquivo de
# texto simples. O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from interface import *
from arquivo import *
from time import sleep

arq = 'pessoas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    op = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if op == 1:
        head('PESSOAS CADASTRADAS')
        lerArquivo(arq)
    elif op == 2:
        head('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif op == 3:
        head('Saindo do Sistema... Até logo!')
        break
    sleep(1)
