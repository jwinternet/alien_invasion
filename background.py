#!/usr/bin/env python3
"""Alien Invasion - Background Module"""

__author__ = "Jared Winter"
__started__ = "2/24/2021"
__revision__ = "v1.1.0"

import pygame
from pygame.sprite import Sprite


class Background(Sprite):
	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/space.jpg')
		self.rect = self.image.get_rect()

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
