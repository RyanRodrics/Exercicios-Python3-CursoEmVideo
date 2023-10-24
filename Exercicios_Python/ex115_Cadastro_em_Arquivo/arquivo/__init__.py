from ex115_Cadastro_em_Arquivo.lib.interface import *


def arquivoExiste(arqNome):
    try:
        a = open(arqNome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arqNome):
    try:
        a = open(arqNome, 'wt+')
        a.close()
    except Exception as erro:
        print(f'{cor(1)}Houve um erro na criação do arquivo!{cor(0)} ', erro.__class__)
    else:
        print(f'Arquivo {arqNome} criado com sucesso!')


def lerArquivo(arqNome):
    try:
        a = open(arqNome, 'rt')
    except Exception as erro:
        print(f'{cor(1)}Erro ao abrir o arquivo!{cor(0)} ', erro.__class__)
    else:
        for linha in a:
            pessoa = linha.split(';')
            pessoa[1] = pessoa[1].replace('\n', '')
            print(f'{pessoa[0]:<35}{pessoa[1]:>10} anos')
    finally:
        a.close()


def cadastrar(arqNome, nome='desconhecido', idade=0):
    try:
        a = open(arqNome, 'at')
    except Exception as erro:
        print(f'{cor(1)}Erro ao abrir o arquivo!{cor(0)} ', erro.__class__)
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except Exception as erro:
            print(f'{cor(1)}Erro ao escrever no arquivo!{cor(0)} ', erro.__class__)
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
