import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 1300, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Vampi Game")

# Configuración del fondo
background = pygame.image.load('static/dark_background.jpg')
background = pygame.transform.scale(background, (width, height))

player_image = pygame.image.load('static/vampi-removebg-preview.png')
scale_percent = 25  # Scale the image by a percentage
new_width = int(player_image.get_width() * scale_percent / 100)
new_height = int(player_image.get_height() * scale_percent / 100)
scaled_image = pygame.transform.scale(player_image, (new_width, new_height))  # Resize the image

# Configuración del jugador
player_size = 40
player_x = width // 2
player_y = height // 2
player_speed = 5

# Reloj para controlar la velocidad de actualización.
clock = pygame.time.Clock()

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - new_width:  # Ajustar para tener en cuenta el ancho de la imagen
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < height - new_height:  # Ajustar para tener en cuenta la altura de la imagen
        player_y += player_speed

    # Dibujar fondo
    screen.blit(background, (0, 0))

    # Dibujar jugador
    screen.blit(scaled_image, (player_x, player_y))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    clock.tick(60)
