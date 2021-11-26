import pygame, sys

sixPixel_font = None
dogicapixel_font = None
pixelart_font = None
bg_game = None
bg_main = None
head_sprite = None
hearts_sprite = None
player_sprite = None
robort_sprite = None
title_sprite = None
trash_sprite = None
trashcans_sprite = None

# Load all game assets
def load():
    global sixPixel_font, dogicapixel_font, pixelart_font
    # Load ingame fonts
    sixPixel_font = pygame.font.Font("./assets/6px-Normal.ttf", 8)
    dogicapixel_font = pygame.font.Font("./assets/dogicapixel.ttf", 8)
    pixelart_font = pygame.font.Font("./assets/pixelart.ttf", 8)

    global bg_game, bg_main
    global head_sprite, hearts_sprite
    global robort_sprite, title_sprite
    global player_sprite, trashcans_sprite
    global trash_sprite
    # Load game sprites
    bg_game = pygame.image.load("./assets/game_bg.tga")
    bg_main = pygame.image.load("./assets/main_bg.tga")
    head_sprite = pygame.image.load("./assets/cabeza.tga")
    hearts_sprite = pygame.image.load("./assets/hearts.tga")
    player_sprite = pygame.image.load("./assets/player.tga")
    robort_sprite = pygame.image.load("./assets/robort.tga")
    title_sprite = pygame.image.load("./assets/title.tga")
    trash_sprite = pygame.image.load("./assets/trash.tga")
    trashcans_sprite = pygame.image.load("./assets/trashcans.tga")