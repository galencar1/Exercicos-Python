"""""""""
nome = input('Qual é seu nome?')
print('Prazer em te conhecer {}!'.format(nome))

print('=' * 20)

# Alinhamentos #

# Alinhamento a direita
nome = input('Qual é seu nome?')
print('Prazer em te conhecer {:>20}!'.format(nome))

print('=' * 20)

# Alinhamento a esquerda
nome = input('Qual é seu nome?')
print('Prazer em te conhecer {:<20}!'.format(nome))

print('=' * 20)

# Centralizado
nome = input('Qual é seu nome?')
print('Prazer em te conhecer {:^20}!'.format(nome))

print('=' * 20)
"""""""""
# Operadores Aritméticos #
n1 = int(input('Um Valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, a subtração é {}, o produto é {} e a divisão é {:.3f} !'.format(s, sb, m, d))
print('A soma é {}, a subtração é {}, o produto é {} e a divisão é {:.3f} !'.format(s, sb, m, d))
print('A Divisão inteira é {} e a potência é {}'.format(di, e))
