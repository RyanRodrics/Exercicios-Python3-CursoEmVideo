# Ex114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except Exception as erro:
    print('Site indisponível no momento')
    print(erro.__class__)
else:
    print('Tudo OK')
    print(site.read)
