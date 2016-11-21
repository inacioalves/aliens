# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 22:57:14 2016

@author: inacio
"""

class Settings():
    def __init__(self):
        self.screen_width  = 1160
        self.screen_height = 710
        self.bg_color      = (230, 230, 230)

        # Configuracoes da nave
        self.ship_speed_factor = 1.5

        # Configuracoes dos projeteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height= 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        # Configuracoes dos alienigenas        
        self.alien_speed_factor = 1
        self.fleet_drop_speed   = 5
        self.fleet_direction    = 1
        self.aliens_separation_x = 1.5
        self.aliens_separation_y = 1.5
        self.aliens_max_y = 4