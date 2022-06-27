km = float(input('Quantos KM foram percorridos com o carro?'))
dia = int(input('Quantos dias o carro permaneceu alugado?'))
preco = (km*0.15)+(dia*60)
print('O Carro foi alugado por {} dias e percorreu {} Km. Total a pagar pelo aluguel é R${:.2f}'.format(dia, km, preco))
