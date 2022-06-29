import random
print('='*25)
print('='*6, 'DESAFIO 028', '='*6)
'''
Escreva um programa que faça
o computador pensar em um número de 0 a 5 
e peça para o usuário tentar adivinhar 
qual foi o número escolhido pelo PC.

O programa deverá escrever na tela
se o usuário vencer ou perdeu.
'''
print('-=--'*20)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar')
print('-=--'*20)
num = [0, 1, 2, 3, 4, 5]
numr = random.choice(num)
n1 = int(input('Digite um número de 0 a 5: '))
if n1 == numr:
    print('Parabéns! Você acertou!')
else:
    print('Não foi dessa vez! Tente novamente.')
print('O Número que pensei foi {}'.format(numr))
