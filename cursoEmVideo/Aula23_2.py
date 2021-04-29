import urllib
import urllib.request

s = str(input('Digite o site que você deseja acessar: '))

try:
    site = urllib.request.urlopen(s)
except:
    print(f'O site ({s}) não está acessivel no momento.')
else:
    print(f'O site ({s}) está acessivel')
