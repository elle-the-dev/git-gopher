from git_gopher.CommandInterface import CommandInterface
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class StashMessage(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        stash_message = self._git_data_getter.get_stash_message_from_input('git stash push -m "[your message here]"')

        if stash_message:
            return self._hist_command_runner.run(['git', 'stash', 'push', '-m', stash_message])
