# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 10:17:55 2016

@author: inacio
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Define uma classe de projeteis disparados pela nave"""
    
    def __init__(self, ai_settings, screen, ship):
        """Cria um projetil para a nave e sua posicao atual atual"""
        super(Bullet, self).__init__()
        self.screen = screen
        
        # Cria um retangulo para o projetil, posicionando em (0, 0) e,
        # em seguida, mudando para a posicao correta
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Armazena a posicao do projetil como um valor decimal
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """Move o projetil para cima na tela"""
        
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Desenha o projetil na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)
