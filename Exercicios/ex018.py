from math import sin, cos, tan, radians
print('='*25)
print('='*6, 'DESAFIO 018', '='*6)
"""""
Faça um programa que leia 
um ângulo e mostre na tela o valor do seno
cosseno e tangente desse ângulo.
"""""
an = float(input('Digite o ângulo que você deseja: '))
se = sin(radians(an))
co = cos(radians(an))
ta = tan(radians(an))
print('O ângulo de {} \ntem o SENO de {:.2f}, \nCOSSENO de {:.2f} \ne a TANGENTE de {:.2f}'.format(an, se, co, ta))
