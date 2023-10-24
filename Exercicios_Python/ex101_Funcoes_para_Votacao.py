# Ex101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de
# uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import datetime
    nascimento = ano
    idade = datetime.now().year - nascimento
    if idade < 16:
        return f'Com {idade} anos, NÃO VOTA'
    elif 16 <= idade <= 17 or idade > 65:
        return f'Com {idade} anos , VOTO OPCIONAL'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos, VOTO OBRIGATÓRIO'


print('-' * 30)
print(voto(int(input('Em que ano você nasceu? '))))
