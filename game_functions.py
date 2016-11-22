# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:36:18 2016

@author: inacio
"""

import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Atualiza as imagens na tela e alterna para a nova tela."""

    # Redesenha a tela
    screen.fill(ai_settings.bg_color)
    # Redesenha todos os projeteis 
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Atualiza com a tela mais recente
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Atualiza a posicao dos bullets e apaga os bullets antigos."""
    # Atualiza a posicao dos projeteis
    bullets.update()
        
    # Destroi os objetos 'bullets' quando eles atingem o topo da tela
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """Checa e exclui 'bullets' e 'aliens' quando estes colidem"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet( ai_settings, screen, ship, bullets ):
    """Dispara um projetil se o limite ainda nao foi atingido"""
    # Cria um novo projetil
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """Cria uma frota completa de aliens."""    
    factor_x = ai_settings.aliens_separation_x
    factor_y = ai_settings.aliens_separation_y

    number_aliens_x = get_number_aliens_x(ai_settings, screen, factor_x)
    row_numbers = get_number_rows(ai_settings, screen, 
                                  ship.rect.height, factor_y)
    
    # Cria uma frota de aliens
    for row_number in range(row_numbers):
        for alien_number in range(number_aliens_x):
            # Cria um novo alien e posiciona ao lado direito do anterior
            aliens.add( create_alien(ai_settings, screen, alien_number, 
                                     row_number, factor_x, factor_y))


def create_alien(ai_settings, screen, alien_number, row_number,
                 factor_x, factor_y):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + factor_x*alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + factor_y*alien.rect.height * row_number
    return(alien)
    #aliens.add(alien)


def check_fleet_edges(ai_settings, aliens):
    """altera a direcao de um alien que chegou a borda"""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            return


def change_fleet_direction(ai_settings, aliens):
    """Faz toda a frota mudar de direcao"""
    for alien in aliens:
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction = -ai_settings.fleet_direction


def update_aliens(ai_settings, aliens):
    """Atualiza as posicoes dos aliens"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


def get_number_aliens_x(ai_settings, screen, factor_x):
    """Determina o numero de aliens que cabem em uma linha"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width    
    available_space = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space / (factor_x*alien_width) )
    return number_aliens_x


def get_number_rows(ai_settings, screen, ship_height, factor_y):
    """Determina o numero de linhas com aliens que cabem na tela"""
    alien = Alien(ai_settings, screen)
    alien_height = alien.rect.height
    available_space = ai_settings.screen_height - 3*alien_height - ship_height
    number_rows = int(available_space / (factor_y*alien_height) )
    #if number_rows > ai_settings.aliens_max_y:
    #    number_rows = ai_settings.aliens_max_y
    return number_rows