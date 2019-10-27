from os import path
from pathlib import Path
from re import sub
from subprocess import run

class GitGopher():
    def __init__(self, command_factory, options):
        self._command_factory = command_factory
        self._options = options

    def process(self, argv: list):
        num_args = len(argv)

        if (num_args < 2):
            cmd = 'menu'
        else:
            cmd = argv[1]

        shortcuts = self._get_shortcuts()
        if cmd in shortcuts.keys():
            return run(shortcuts.get(cmd).split())

        try:
            command = self._command_factory.make(cmd)
            response = command.run()
            if response:
                print(response)
        except AttributeError as e:
            print("Error: Unknown command\n")
            print("Run the following to see a list of commands:\n")
            print("$ ggo")

    def _get_shortcuts(self):
        options = self._options.get().splitlines()

        switcher = {}
        for option in options:
            pieces = option.split('|')
            switcher[pieces[1].strip()] = pieces[0].strip()

        return switcher

