import pygame

"""""
Faça um programa que abra 
e reproduza o áudio de um 
arquivo MP3
"""""
# Utilizando o módulo Py Game para importar música
pygame.init()  # Inicia o módulo.
pygame.mixer.music.load('ex021.mp3')  # carrega a música
pygame.mixer.music.play()  #Toca a música
pygame.event.wait()
