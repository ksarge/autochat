#! /usr/bin/env python

import random
import keyboard
import re
from threading import Thread, Event
from datetime import datetime

import commands


class AlreadyRunningException(Exception):
    pass


class Bot:
    def __init__(self):
        print('initializing Bot ')
        self.t = None
        self.exit_event = Event()
        self.command_pattern = r'{(.*)}'

    def start(self, cmd: str, lower_limit: int, upper_limit: int):
        if self.t:
            raise AlreadyRunningException()

        self.exit_event.clear()
        self.t = Thread(target=Bot.bot, args=(self, cmd, lower_limit, upper_limit))
        self.t.start()

    def stop(self):
        self.exit_event.set()
        if self.t:
            self.t.join()
            self.t = None
        else:
            print('nothing to stop, bot is already inactive.')

    @staticmethod
    def validate_limits(lower, upper):
        return upper > lower

    def validate_command(self, cmd):
        subcmds = cmd.split(';')
        for sub in subcmds:
            script = self.get_script(sub)
            if script:
                cmd_name = script.split(' ')[0]
                if not commands.registry.get(cmd_name):
                    print(f'{cmd_name} not found in the command registry')
                    return False
        return True

    def get_script(self, cmd):
        match = re.search(self.command_pattern, cmd)
        if match:
            return match.group(1)
        return None

    def bot(self, cmd: str, lower_limit: int, upper_limit: int):
        """
        lower_limit and upper_limit are in minutes
        """
        print('starting bot in 5 seconds')
        self.exit_event.wait(5)

        while not self.exit_event.is_set():
            subcmds = cmd.split(';')
            print(f'[{datetime.now()}] running command', subcmds)
            for sub in subcmds:
                script = self.get_script(sub)
                if script:
                    commands.execute(script)
                else:
                    keyboard.write(sub + '\n')
            duration = random.randrange(lower_limit, upper_limit)
            print(f'[{datetime.now()}] sleeping for {duration / 60} minutes')
            self.exit_event.wait(duration)

        print('stopping bot. goodbye.')
