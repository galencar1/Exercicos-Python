frase = 'Curso em Vídeo Python'
frase2 = '    Curso em Vídeo Python     '
frase3 = 'Curso em Vídeo Python'
print(frase)
print(frase[3])  # Imprime a quarta letra
print(frase[3:13])  # Fatiar - IMprime da 4ª letra até a 12ª(Excluindo a 13)
print(frase[:13])  # Do inicio até a letra 12
print(frase[13:])  # A partir do 13 até o final
print(frase[1:15:2])  # pulando de dois em dois
print(frase[:15:2])  # Do inicio até a 15 pulando de 2 em 2
print(frase[::3])  # Do inicio até o final pulando de 3 em 3

print(frase.count('o'))  # Conta quantas vezes tem 'o'
print(frase.count('O'))  # conta os 'O' maiusculo
print(frase.upper().count('O'))  # JOga a frase para maiusculo e conta quantas vezes tem 'O'
print(len(frase))  # Revela o tamanho da string(Conta os espaços)
print(len(frase2))  # Essa frase possui espaços
print(len(frase2.strip()))  # STRIP remove os espaços antes e depois
print(frase.replace('Python', 'Android'))  # Substitui a palavra python por android
print('Curso' in frase)  # Verifica se a palavra curso está na String frase(Retorna True or False)
print(frase.find('Vídeo'))  # Mostra a posição em que a palavra se encontra dentro da frase
print(frase.find('vídeo'))  # Caso a palavra não exista na frase ele retorna -1
print(frase.split())  ## Divide a frase em uma lista para cada palavra

