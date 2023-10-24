# Ex105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:

def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ounão adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['Quantidade de notas'] = len(notas)
    r['Maior nota'] = max(notas)
    r['Menor nota'] = min(notas)
    r['Média'] = sum(notas)/len(notas)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


print(notas(7, 10, 8, 3, 5, 7, sit=True))
help(notas)
