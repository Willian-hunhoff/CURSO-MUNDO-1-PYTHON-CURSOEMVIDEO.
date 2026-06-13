import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load('vidan.mp3')
pygame.mixer.music.play(True)
while pygame.mixer.music.get_busy():
    time.sleep(1)
