# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:36:18 2016

@author: inacio
"""

import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Cria um novo projetil
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
                

def update_screen(ai_settings, screen, ship, bullets):
    """Atualiza as imagens na tela e alterna para a nova tela."""

    # Redesenha a tela
    screen.fill(ai_settings.bg_color)
    # Redesenha todos os projeteis 
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Atualiza com a tela mais recente
    pygame.display.flip()
