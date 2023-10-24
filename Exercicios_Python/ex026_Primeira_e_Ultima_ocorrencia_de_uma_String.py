# Ex026: Faça um programa que leia uma frase pelo teclado e mostre:
# --> Quantas vezes aparece a letra "A";
# --> Em que posição ela aparece a primeira vez;
# --> Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).lower().strip()
# print('A letra "a" aparece {} vezes'.format(int(frase.count('a')) + int(frase.count('A'))))
print('A letra "a" aprece {} vezes'.format(frase.count('a')))
print('A letra "a" aparece pela primeira vez na posição', frase.find('a') + 1)
# ultima = int(len(minuscula)) + 1
print('A letra "a" aparece pela última vez na posição', frase.rfind('a') + 1)
