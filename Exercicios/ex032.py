print('='*25)
print('='*6, 'DESAFIO 032', '='*6)
'''
Faça um programa que 
leia um ano qualquer e 
mostre se le é BISSEXTO
'''
ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    print('Esse é um ano bissexto.')
else:
    print('Esse não é um ano bissexto!')
