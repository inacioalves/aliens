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

def run_game():
    # Inicia o jogo e cria um objeto tela
    pygame.init()
    ai_settings = Settings()    
    screen = pygame.display.set_mode(
        (ai_settings.screen_witdh,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Cria uma nave
    ship = Ship(screen)
    
    # Laco principal do jogo
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

run_game()