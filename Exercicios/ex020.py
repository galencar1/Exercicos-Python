from random import shuffle
print('='*25)
print('='*6, 'DESAFIO 020', '='*6)
"""""
Um professor quer sortear a ordem 
de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome
dos quatro alunos e mostre a ordem
sorteada
"""""
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A Ordem de apresentação será {}'.format(lista))
