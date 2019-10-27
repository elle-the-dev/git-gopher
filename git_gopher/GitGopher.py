from os import path
from pathlib import Path
from re import sub

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

        long_cmd = self._shortcut_to_long(cmd)
        try:
            command = self._command_factory.make(long_cmd)
            response = command.run()
            if response:
                print(response)
        except AttributeError as e:
            print("Error: Unknown command\n")
            print("Run the following to see a list of commands:\n")
            print("$ ggo")

    def _shortcut_to_long(self, shortcut: str):
        options = self._options.get().splitlines()

        switcher = {}

        for option in options:
            pieces = option.split('|')
            switcher[pieces[1].strip()] = sub(r'^ggo ', '', pieces[0].strip())

        if shortcut in switcher.keys():
            return switcher.get(shortcut)

        return shortcut
