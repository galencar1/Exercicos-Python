print('======DESAFIO 011======')
"""""
Programa lê a largura e altura de uma parede
calcula sua área e a quantidade de tinta
necessária para pintá-la, sabendo que 
cada litro de tinta pinta uma área de 2m²
"""""
l = float(input('Qual é a largura da parede? '))
a = float(input('Qual é a altura da parede?'))
ar = l * a
tl = ar / 2
print('A Área da parede é {}, e para pintá-la serão necessários {:.2f} litros de tinta'.format(ar, tl))
############################################################################################
