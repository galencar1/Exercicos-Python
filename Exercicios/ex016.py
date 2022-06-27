import math

print('='*25)
print('='*6, 'DESAFIO 016', '='*6)
"""""
Crie um programa que leia
um número real qualquer e
mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127
O Número 6.127 tem a parte inteira 6.
"""""
print('Quebrando um número!')
n1 = float(input('Digite um número real: '))
print('O número real {} tem a parte inteira com o valor {}.'.format(n1, math.trunc(n1)))
