from os import path
from pathlib import Path
from colorama import Fore
from pydoc import pager
from gitgud.CommandInterface import CommandInterface
from gitgud.FormatColumns import FormatColumns

class History(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        history_path = path.expanduser("~") + "/.config/git-gud/history"

        if not path.exists(history_path):
            return "No git-gud history found"

        history = Path(history_path).read_text().splitlines()
        history.reverse()
        history = '\n'.join(history)
        format_columns = FormatColumns()
        return pager(format_columns.set_colors({ 0: Fore.BLUE, 1: Fore.YELLOW }).format(history))
