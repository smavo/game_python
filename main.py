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
jugador_x_cambio = 0

def jugador(x, y):
    pantalla.blit(tilincha, (x, y))

# Loop del Juego
se_ejecuta = True

while se_ejecuta:
    # RGB
    pantalla.fill((205,144,255))
    # jugador_x += 0.1
    # jugador_y += -0.1

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:
            # print("Una de las teclas fue seleccionada")
            if evento.key == pygame.K_LEFT:
                # print("Tecla izquierda presionada")
                jugador_x_cambio = -0.1
            if evento.key == pygame.K_RIGHT:
                # print("Tecla Derecha presionada")
                jugador_x_cambio = 0.1
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                # print("Se solto la flecha")
                jugador_x_cambio = 0

    jugador_x += jugador_x_cambio
    jugador(jugador_x, jugador_y)

    pygame.display.update()