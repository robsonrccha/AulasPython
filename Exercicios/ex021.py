#AULA 08

#FAÇA UM PROGRAMA QUE ABRA E REPRODUZA O AUDIO DE UM ARQUIVO MP3

import pygame
import time  #PARA CONTROLAR O TEMPO DE REPRODUÇÃO

#INICIALIZAÇÃO
pygame.init()
pygame.mixer.init()

#CARREGAR E TOCAR O ÁUDIO
pygame.mixer.music.load('ex021_superposition.mp3')
pygame.mixer.music.set_volume(0.5)  #VOLUME DE 0.0 A 1.0
pygame.mixer.music.play()

#ESPERAR ATÉ QUE A MÚSICA TERMINE
while pygame.mixer.music.get_busy():
    time.sleep(1)  #AGUARDA 1 SEGUNDO E VERIFICA DE NOVO
