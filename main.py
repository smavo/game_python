import pygame

# Inicializa Pygame
pygame.init()

# Pantalla y dimenciones
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption("Invasion de amor")
icono = pygame.image.load("avion-de-papel.png")
pygame.display.set_icon(icono)

# Loop del Juego
se_ejecuta = True

while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
    pantalla.fill((205,144,255))
    pygame.display.update()