##Tipos primitivos, saída de dados e dissecação de variável.##
n = input('Digite algo: ')
print('O valor digitado foi {} e é do tipo primitivo {}.'.format(n, type(n)))
print('É alfanum? {}'.format(n.isalnum()))
print('É Alfabeto? {}'.format(n.isalpha()))
print('É ASCII? {}'.format(n.isascii()))
print('É um dígito? {}'.format(n.isdigit()))
print('É minuscula? {}'.format(n.islower()))
print('É Decimal? {}'.format(n.isdecimal()))
print('É númerico? {}'.format( n.isnumeric()))
print('É possível imprimir? {}'.format(n.isprintable()))
print('É espaço? {}'.format(n.isspace()))
print('É Capitalizada? {}'.format(n.istitle()))
print('É maiuscula? {}'.format(n.isupper()))
