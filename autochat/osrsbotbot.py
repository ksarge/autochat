#! /usr/bin/env python

import random
import keyboard
import time
from threading import Thread, Event
from datetime import datetime


class AlreadyRunningException(Exception):
	pass


class Bot:
	def __init__(self):
		print('initializing Bot ')
		self.t = None
		self.exit = Event()

	def start(self, cmd: str, lower_limit: int, upper_limit: int):
		if self.t:
			raise AlreadyRunningException()

		self.exit.clear()
		self.t = Thread(target=Bot.bot, args=(self, cmd, lower_limit, upper_limit))
		self.t.start()

	def stop(self):
		self.exit.set()
		if self.t:
			self.t.join()
			self.t = None
		else:
			print('nothing to stop, bot is already inactive')

	def bot(self, cmd: str, lower_limit: int, upper_limit: int):
		"""
		lower_limit and upper_limit are in minutes
		"""
		print('starting bot in 5 seconds')
		time.sleep(5)

		self.active = True

		while not self.exit.is_set():
			keyboard.write(cmd + '\n')
			tts = random.randrange(lower_limit, upper_limit)
			print(f'[{datetime.now()}] sleeping for {tts / 60} minutes')
			self.exit.wait(tts)

		print('stopping bot. goodbye.')