#!/usr/bin/env python

import pygame

class Ship():
    def __init__(self, screen):
        """Inicia uma espaconave e define sua posicao inicial"""
        self. screen = screen

        # Carrega a imagem da nave
        self.image = pygame.image.load('images/ship.bmp')
        self.rect  = self.image.get_rect()
        self.screen_rect = screen.get_rect()
    
        # Inicia cada nova nave na parte inferior
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.bottom
        
        # Flags de movimento
        self.moving_right = False
        self.moving_left  = False

    def blitme(self):
        """Desenha a nave em sua posicao atual."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Atualiza a posicao da nave de acordo com as flags
           de movimento"""
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1