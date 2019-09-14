import pygame
import random

pygame.init()

# initialise les variables
largeur_fenetre = 1000
hauteur_fenetre = 1000
x = 100
y = 100
largeur = 50
hauteur = 50
vitesse = 2
couleur_fond = (0, 0, 0)
couleur = (0, 200, 0)

# initialise la fenetre
win = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("bug")

# boucle principale
run = True
while run:
    pygame.time.delay(10)

    # teste la sortie
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # action clavier
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = x - vitesse
    if keys[pygame.K_RIGHT]:
        x = x + vitesse
    if keys[pygame.K_UP]:
        y = y - vitesse
    if keys[pygame.K_DOWN]:
        y = y + vitesse
    if keys[pygame.K_c]:
        couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if x < 0:
        x = 0
    if x > largeur_fenetre - largeur:
        x = largeur_fenetre - largeur
    if y < 0:
        y = 0
    if y > hauteur_fenetre - hauteur:
        y = hauteur_fenetre - hauteur

    win.fill(couleur_fond)

    pygame.draw.rect(win, couleur, (x, y, largeur, hauteur))
    pygame.display.update()
