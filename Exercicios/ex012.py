print('======DESAFIO 012======')
"""""
Programa lê o preço do produto 
e mostre seu novo preço com 5% de desconto.
"""""
n1 = float(input('Digite o preço do produto: R$'))
n2 = n1 - (n1 * 5/100)
print('O Valor digitado foi {}. Com 5% de desconto passará a ser {:.2f}'.format(n1, n2))
############################################################################################
