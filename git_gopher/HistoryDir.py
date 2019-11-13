from os import path, getcwd
from pathlib import Path
from colorama import Fore
from pydoc import pager
from git_gopher.CommandInterface import CommandInterface
from git_gopher.FormatColumns import FormatColumns
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class HistoryDir(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        history_path = path.expanduser("~") + "/.config/git-gopher/history"
        cwd = getcwd()

        if not path.exists(history_path):
            return "No git-gopher history found"

        history = list(filter(lambda line: cwd in line, Path(history_path).read_text().splitlines()))
        history.reverse()
        history = '\n'.join(history)
        format_columns = FormatColumns()
        return pager(format_columns.set_colors({ 0: Fore.BLUE, 1: Fore.YELLOW }).format(history))
