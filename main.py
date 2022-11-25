import pygame

# Inicializa Pygame
pygame.init()

# Pantalla y dimenciones
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption("Invasion de amor")
icono = pygame.image.load("avion-de-papel.png")
pygame.display.set_icon(icono)

# Jugador
tilincha = pygame.image.load("mujer.png")
jugador_x = 368
jugador_y = 536

def jugador():
    pantalla.blit(tilincha, (jugador_x, jugador_y))

# Loop del Juego
se_ejecuta = True

while se_ejecuta:
    # RGB
    pantalla.fill((205,144,255))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    jugador()

    pygame.display.update()