from git_gopher.CommandInterface import CommandInterface
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class StashDrop(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        stash = self._git_data_getter.get_stash_ref(preview='echo "git stash drop {1}"')

        if stash:
            return self._hist_command_runner.run(['git', 'stash', 'drop', stash])
