print('='*25)
print('='*6, 'DESAFIO 033', '='*6)
'''
Faça um programa que leia
três números e mostre qual é
o maior e qual é o menor.
'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

menor = num1
if num2<num3 and num2<num1:
    menor = num2
if num3<num2 and num3<num1:
    menor = num3

maior = num1
if num2>num3 and num2>num1:
    maior = num2
if num3>num2 and num3>num1:
    maior = num3
print('O maior valor digitado foi {} e o menor valor digitado foi: {}'.format(maior, menor))
