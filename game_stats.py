"""
Alien Invasion Game Stats Module
"""
###############################################################################

__author__ = "Jared Winter"
__copyright__ = "Copyright 2020, jwinternet"
__credits__ = ""
__license__ = "GNU General Public License v3.0"
__version__ = "1.0.0"
__updated__ = "3/6/2020"
__email__ = "jaredwinter2015@outlook.com"
__status__ = "DEV"

###############################################################################

class GameStats:
	"""Track statistics for Alien Invasion."""
	def __init__(self, ai_game):
		"""Initialize statistics."""
		self.settings = ai_game.settings
		self.reset_stats()

		# Start game in an inactive state.
		self.game_active = False

		# High score should never be reset.
		self.high_score = 0

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1