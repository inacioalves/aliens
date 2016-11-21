# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 22:57:14 2016

@author: inacio
"""

class Settings():
    def __init__(self):
        self.screen_witdh  = 960
        self.screen_height = 710
        self.bg_color      = (230, 230, 230)
        
        # Configuracoes da nave
        self.ship_speed_factor = 1.5
        
        # Configuracoes dos projeteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height= 15
        self.bullet_color = (60,60,60)
