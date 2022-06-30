print('='*25)
print('='*6, 'DESAFIO 029', '='*6)
'''
Escreva um programa
que leia a velocidade de um carro.

Se ele ultrapassar 80KM/H
mostre uma msg dizendo que 
ele foi multado.

A multa vai custar R$ 7,00
por cada KM acima do Limite.
'''
vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    print('Você foi multado.')
    multa = (vel-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Você estava a {} Km/h.'.format(vel))
