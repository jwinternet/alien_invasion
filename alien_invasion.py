"""
Alien Invasion Primary Module
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

import sys
import pygame
import settings
import ship

###############################################################################

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		self.settings = settings.Settings()

		self.screen = pygame.display.set_mode(
				(
					self.settings.screen_width,
					self.settings.screen_height
					)
				)
		pygame.display.set_caption("Alien Invasion")

		self.ship = ship.Ship(self)

	def run_game(self):
		"""Start the main look for the game."""
		while True:
			# Watch for keyboard and mouse events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# Redraw the screen during each pass through the loop.
			self.screen.fill(self.settings.bg_color)
			self.ship.blitme()

			# Make the most recently drawn screen visible.
			pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()
