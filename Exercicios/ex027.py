print('='*25)
print('='*6, 'DESAFIO 027', '='*6)
'''
Programa le o nome
completo de uma pessoa,
mostrando em seguida
o primeiro e o ultimo nome
separadamente
Ex: Ana Maria de Souza
primeiro = Ana
Ultimo = Souza
'''
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Seu nome completo é {},\n o primeiro nome é {},\n e o último nome é {}.'
      .format(nome, n[0], n[len(n)-1]))
