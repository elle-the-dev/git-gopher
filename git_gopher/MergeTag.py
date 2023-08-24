from git_gopher.CommandInterface import CommandInterface
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class MergeTag(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        tag = self._git_data_getter.get_tag_name(preview='echo "git merge {2}"')

        if tag:
            return self._hist_command_runner.run(['git', 'merge', tag])
