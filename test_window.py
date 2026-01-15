import pygame
import sys

pygame.init()
print("Pygame initialized...")
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Test Window")
print("Window created - if you don't see it, check your taskbar!")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()