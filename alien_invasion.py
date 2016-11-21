#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:59:46 2016

@author: inacio
"""

import sys
import pygame

from settings import Settings
from ship import Ship


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
        
        # Observador de eventos
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        
        # Redesenha a tela
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        pygame.display.flip()

run_game()