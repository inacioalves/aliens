# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:29:47 2016

@author: inacio
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Uma classe para representar um alienigena da frota"""

    def __init__(self, ai_settings, screen):
        """Inicializa um alienigena e define a posicao inicial do mesmo"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Carrega a imagem do alien
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Inicia cada alienigena no canto superior esquerdo da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Armazena a posicao exata do alienigena
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha o alien na posicao atual"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        self.x += (self.ai_settings.alien_speed_factor*
                    self.ai_settings.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True