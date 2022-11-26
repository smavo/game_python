import pygame
import random
import math

# Inicializa Pygame
pygame.init()

# Pantalla y dimenciones
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption("Invasion de amor")
icono = pygame.image.load("avion-de-papel.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")

# Variables del Jugador
tilincha = pygame.image.load("mujer.png")
jugador_x = 368
jugador_y = 530
jugador_x_cambio = 0

# Variables del Enemigo
corazon = pygame.image.load("corazon.png")
enemigo_x = random.randint(0,736)
enemigo_y = random.randint(50,250)
enemigo_x_cambio = 0.5
enemigo_y_cambio = 50

# Variables de la bala
bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 530
bala_x_cambio = 0
bala_y_cambio = 2
bala_visible = False

# Variable puntaje
puntaje = 0

# Funcion Jugador
def jugador(x, y):
    pantalla.blit(tilincha, (x, y))

# Funcion Enemigo
def enemigo(x,y):
    pantalla.blit(corazon, (x, y))

# Funcion disparar
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(bala, (x + 16, y + 10))

# Funcion Detectar colisones
def es_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distancia < 27:
        return True
    else:
        return False

# Loop del Juego
se_ejecuta = True

while se_ejecuta:
    # RGB
    # pantalla.fill((205,144,255))
    pantalla.blit(fondo, (0,0))
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
            elif evento.key == pygame.K_RIGHT:
                # print("Tecla Derecha presionada")
                jugador_x_cambio = 0.1
            elif evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # Evento detectar soltar flecha
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                # print("Se solto la flecha")
                jugador_x_cambio = 0

    # Modificar ubicacion del Jugador
    jugador_x += jugador_x_cambio

    # Mantener dentro de la pantalla al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Modificar Ubicacion del enemigo
    enemigo_x += enemigo_x_cambio

    # Mantener dentro de la pantalla al jugador
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.2
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -0.2
        enemigo_y += enemigo_y_cambio

    # Movimiendo Bala
    if bala_y <= -64:
        bala_y = 530
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # Colision
    colision = es_colision(enemigo_x, enemigo_y,bala_x, bala_y)
    if colision:
        bala_y = 530
        bala_visible = False
        puntaje += 1
        print(puntaje)
        enemigo_x = random.randint(0, 736)
        enemigo_y = random.randint(50, 250)

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    # Actualizar
    pygame.display.update()