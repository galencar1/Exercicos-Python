print('======DESAFIO 013======')
"""""
Programa lê o salário de um funcionário 
e mostre seu novo salário com 15% de aumento.
"""""
n1 = float(input('Digite seu salário: '))
n2 = n1 + (n1 * 15/100)
print('Seu novo salário será {:.2f}'.format(n2))
