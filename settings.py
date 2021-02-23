#!/usr/bin/env python3
"""Alien Invasion - Settings Module"""

__author__ = "Jared Winter"
__started__ = "2/23/2021"
__revision__ = "v0.0.1"


class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1450
		self.screen_height = 750
		self.bg_color = (230, 230, 230)
