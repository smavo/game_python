import pygame
import random
import math
from pygame import mixer

# Inicializa Pygame
pygame.init()

# Pantalla y dimenciones
pantalla = pygame.display.set_mode((800, 600))

# Agregar Musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

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
corazon = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    corazon.append(pygame.image.load("corazon.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,250))
    enemigo_x_cambio.append(0.6)
    enemigo_y_cambio.append(50)

# Variables de la bala
bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 530
bala_x_cambio = 0
bala_y_cambio = 4
bala_visible = False

# Variable puntaje
puntaje = 0
# fuente = pygame.font.Font('freesansbold.ttf', 32)
fuente = pygame.font.Font('11S0BLT_.TTF', 31)
text_x = 10
text_y = 10

# Funcion Mostrar Puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))
    pantalla.blit(texto, (x, y))

# Funcion Jugador
def jugador(x, y):
    pantalla.blit(tilincha, (x, y))

# Funcion Enemigo
def enemigo(x,y, ene):
    pantalla.blit(corazon[ene], (x, y))

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
                jugador_x_cambio = -0.8
            elif evento.key == pygame.K_RIGHT:
                # print("Tecla Derecha presionada")
                jugador_x_cambio = 0.8
            elif evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # Evento detectar soltar flecha
        if evento.type == pygame.KEYUP:
            sonido_bala = mixer.Sound('disparo.mp3')
            sonido_bala.play()
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
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]

        # Mantener dentro de la pantalla al jugador
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.2
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.2
            enemigo_y[e] += enemigo_y_cambio[e]

        # Colision
        colision = es_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            bala_y = 530
            bala_visible = False
            puntaje += 1
            # print(puntaje)
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 250)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiendo Bala
    if bala_y <= -64:
        bala_y = 530
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)

    mostrar_puntaje(text_x, text_y)

    # Actualizar
    pygame.display.update()