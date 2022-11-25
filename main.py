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

# Variables
jugador_x = 368
jugador_y = 530
jugador_x_cambio = 0

# Funcion Jugador
def jugador(x, y):
    pantalla.blit(tilincha, (x, y))

# Loop del Juego
se_ejecuta = True

while se_ejecuta:
    # RGB
    pantalla.fill((205,144,255))
    # jugador_x += 0.1
    # jugador_y += -0.1

# Iterar Eventos
    for evento in pygame.event.get():

        # Evento Cerrar programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento detectar movimiento de flechas
        if evento.type == pygame.KEYDOWN:
            # print("Una de las teclas fue seleccionada")
            if evento.key == pygame.K_LEFT:
                # print("Tecla izquierda presionada")
                jugador_x_cambio = -0.1
            if evento.key == pygame.K_RIGHT:
                # print("Tecla Derecha presionada")
                jugador_x_cambio = 0.1

        # Evento detectar soltar flecha
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                # print("Se solto la flecha")
                jugador_x_cambio = 0

    # Modificar Jugador
    jugador_x += jugador_x_cambio

    # Mantener dentro de la pantalla al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    jugador(jugador_x, jugador_y)

    # Actualizar
    pygame.display.update()