"""
Alien Invasion Ship Module
"""
###############################################################################

__author__ = "Jared Winter"
__copyright__ = "Copyright 2020, jwinternet"
__credits__ = ""
__license__ = "GNU General Public License v3.0"
__version__ = "0.0.1"
__updated__ = "3/3/2020"
__email__ = "jaredwinter2015@outlook.com"
__status__ = "DEV"

###############################################################################

import pygame

###############################################################################

class Ship:
	"""A class to manage the ship."""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
