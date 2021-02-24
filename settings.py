#!/usr/bin/env python3
"""Alien Invasion - Settings Module"""

__author__ = "Jared Winter"
__started__ = "2/23/2021"
__revision__ = "v0.2.0"


class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1050
		self.screen_height = 650
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.5

		# Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 8
