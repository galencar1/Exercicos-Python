print('='*25)
print('='*6, 'DESAFIO 026', '='*6)
'''
Le uma frase pelo teclado
e mostre:
-> Quantas vezes aparece a letra A
-> Em que posição ela aparece na primeira vez.
-> Em que posição aparece a última vez
'''
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "a" aparece {} vez(es)'.format(frase.count('A')))
print('Ela aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('Ela aparece pela última vez na posição {}'.format(frase.rfind('A')+1))
