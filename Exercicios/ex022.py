print('='*25)
print('='*6, 'DESAFIO 022', '='*6)
'''
Crie um programa que leia
o nome completo de uma 
pessoa e mostre:

-> Nome com todas as letras maiusculas
-> Nome com todas as letras minusculas
-> Quantas letras ao todo(sem considerar espaços)
-> Quantas letras tem o primeiro nome
'''
nome = str(input('Digite seu nome: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
print(nome.find(' '))
