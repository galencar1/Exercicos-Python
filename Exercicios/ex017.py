import math

print('='*25)
print('='*6, 'DESAFIO 017', '='*6)
"""""
Faça um programa que
leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo,
retângulo, calcule e mostre o comprimento da hipotenusa.
"""""
print('Catetos e Hipotenusa')
b = float(input('Digite o valor do cateto oposto: '))
c = float(input('Digite o valot do cateto adjacente: '))
print('O valor do cateto oposto é {} e do cateto adjacente é {}, logo a hipotenusa vale {:.2f}.'
      .format(b, c, math.hypot(b, c)))
