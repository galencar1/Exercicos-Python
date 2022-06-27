print('======DESAFIO 010======')
"""""
Programa lê quanto pessoa tem na carteira
e converte para dólares
Considere USS 1,00 = R$ 5,22
"""""
n1 = float(input('Quanto dinheiro você tem na carteira? R$'))
n2 = n1 / 5.22
print('Você possui R${}. Com esse valor é possível comprar U$${:.2f} .'.format(n1, n2))
############################################################################################
