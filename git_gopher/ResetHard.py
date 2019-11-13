from git_gopher.CommandInterface import CommandInterface
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class ResetHard(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        hash = self._git_data_getter.get_commit_hash(preview='echo "git reset --hard {1}"')

        if hash:
            return self._hist_command_runner.run(['git', 'reset', '--hard', hash])
