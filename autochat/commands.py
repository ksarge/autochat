"""
Custom commands that can be called from the bot
"""
import time


def execute(script):
    args = script.split(' ')
    script_name = args.pop(0)

    function = registry[script_name]

    function(*args)


def sleep(*args):
    time.sleep(float(args[0]))
    return


registry = dict(
    sleep=sleep
)
