# Ex024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "SANTO".

cidade = str(input('Digite o nome de uma cidade: ')).strip()
# primeiro = cidade.split()[0]
CID = cidade.upper()
print('Essa cidade começa com "Santo"?', 'SANTO' in CID.split()[0])
