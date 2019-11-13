from os import path
from pathlib import Path
from subprocess import run
from colorama import Fore, Back, Style
from git_gopher.CommandInterface import CommandInterface
from git_gopher.FormatColumns import FormatColumns
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.Fzf import Fzf
from git_gopher.Options import Options

class Menu(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, fzf: Fzf, options: Options):
        self._hist_command_runner = hist_command_runner
        self._fzf = fzf
        self._options = options

    def run(self):
        options = self._options.get()

        format_columns = FormatColumns()
        result = self._fzf.run(format_columns.set_colors({0: Fore.BLUE, 1: Fore.YELLOW}).format(options))

        command = self._get_column(result, 0)
        process = run(command.split())

    def _get_column(self, line: str, column: int):
        return line.split('\t')[0].strip()
