import pygame
import sys
import random

pygame.init()

LATIME, INALTIME = 600, 400
DIMENSIUNE_SPACE = 20

NEGRU = (0,0,0)
ROSU = (255, 0, 0)
VERDE = (0, 255, 255)

ecran = pygame.display.set_mode((LATIME, INALTIME))
pygame.display.set_caption("Jocul de labirint")

sarpe = [(100, 50), (90, 50), (80, 50)]
directie_sarpe = "DREAPTA"

