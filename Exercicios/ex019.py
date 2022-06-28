from random import choice
print('='*25)
print('='*6, 'DESAFIO 019', '='*6)
"""""
Um professor quer sortear um dos seus alunos para apagar o quadro.
Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido.
"""""
print('Sorteando um item na lista')
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O Aluno escolhido foi {}!'.format(escolhido))
