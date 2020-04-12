#! /usr/bin/env python

import random
import keyboard
import time
import fire
from datetime import datetime


def bot(cmd):
	print('starting')
	time.sleep(5)

	while True:
		keyboard.write(cmd + '\n')
		tts = random.randrange(1860, 1960)
		print(f'[{datetime.now()}] sleeping for {tts / 60} minutes')
		time.sleep(tts)

if __name__ == '__main__':
	fire.Fire(bot)
