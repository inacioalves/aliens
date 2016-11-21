#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:59:46 2016

@author: inacio
"""

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    # Inicia o jogo e cria um objeto tela
    pygame.init()
    ai_settings = Settings()    
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma nave
    ship = Ship(ai_settings, screen)

    # Cria um grupo (lista) de Bullets
    bullets = Group()
    
    # Cria um alien
    aliens  = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Laco principal do jogo
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
