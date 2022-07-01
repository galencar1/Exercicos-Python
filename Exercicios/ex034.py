print('='*25)
print('='*6, 'DESAFIO 034', '='*6)
'''
Escreva um programa que 
calcule o salário de um funcionário e 
calcule o valor de seu aumento.

Para salários superiores a R$ 1250,00
calcule um aumento de 10%.

para inferiores ou iguais, o aumento
é de 15%.
'''
salario = float(input('Digite o valor do salário: R$'))
dez = salario * (10/100)
quinze = salario * (15/100)
if salario > 1250:
    salario10 = salario + dez
    print('Seu salário atual é R${} e passou a ser R${:.2f}'.format(salario, salario10))
else:
    salario15 = quinze + salario
    print('Seu salário atual é R${} e passou a ser R${:.2f}'.format(salario, salario15))
