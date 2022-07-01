print('='*25)
print('='*6, 'DESAFIO 031', '='*6)
'''
Desenvolva um programa que pergunte
a distância de uma viagem em KM.
Calcule o preço da passagem,
cobrando R$ 0,50 por KM 
para viagens até 200KM
e R$ 0,45 para viagens mais longas
'''
distancia = float(input('Qual é a distância da viagem? '))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print('O Valor da passagem será R${:.2f}.'.format(passagem))
