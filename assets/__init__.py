import pygame, sys

six_pixel = None
dogicapixel = None
pixelart = None
bg_game = None
bg_main = None
head = None
hearts = None
player = None
robort = None
title = None
trash = None
trashcans = None

# Load all game assets
def load():
    global six_pixel, dogicapixel, pixelart
    global bg_game, bg_main
    global head, hearts
    global robort, title
    global player, trashcans
    global trash
    # Load ingame fonts
    six_pixel = pygame.font.Font("./assets/6px_normal.ttf", 8)
    dogicapixel = pygame.font.Font("./assets/dogicapixel.ttf", 8)
    pixelart = pygame.font.Font("./assets/pixelart.ttf", 8)

    # Load game sprites
    bg_game = pygame.image.load("./assets/game_bg.tga")
    bg_main = pygame.image.load("./assets/main_bg.tga")
    head = pygame.image.load("./assets/cabeza.tga")
    hearts = pygame.image.load("./assets/hearts.tga")
    player = pygame.image.load("./assets/player.tga")
    robort = pygame.image.load("./assets/robort.tga")
    title = pygame.image.load("./assets/title.tga")
    trash = pygame.image.load("./assets/trash.tga")
    trashcans = pygame.image.load("./assets/trashcans.tga")
