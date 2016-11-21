#!/usr/bin/env python

import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """Inicia uma espaconave e define sua posicao inicial"""
        self. screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da nave
        self.image = pygame.image.load('images/ship.bmp')
        self.rect  = self.image.get_rect()
        self.screen_rect = screen.get_rect()
    
        # Inicia cada nova nave na parte inferior
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.bottom
        
        # Armazena um valor decimal para o centro da nave
        self.center = float(self.rect.centerx)
        
        # Flags de movimento
        self.moving_right = False
        self.moving_left  = False

    def blitme(self):
        """Desenha a nave em sua posicao atual."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Atualiza a posicao da nave de acordo com as flags
           de movimento"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # Atualiza o objeto rect
        self.rect.centerx = self.center
