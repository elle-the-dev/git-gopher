from os import path
from pathlib import Path
from subprocess import run
from colorama import Fore, Back, Style

class Options():
    def get(self):
        DIR = path.dirname(path.realpath(__file__))
        custom_options_path = path.expanduser("~") + "/.ggo-options.dat"
        options_path = f"{DIR}/ggo-options.dat"
        options = Path(options_path).read_text()

        if path.exists(custom_options_path):
            options += Path(custom_options_path).read_text()

        return options
