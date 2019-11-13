from git_gopher.CommandInterface import CommandInterface
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class DiffCommits(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        commit1 = self._git_data_getter.get_commit_hash(preview='echo "First of two commits to compare."')

        if not commit1:
            return

        commit2 = self._git_data_getter.get_commit_hash(preview='echo "git diff ' + commit1 + ' {1}"')

        if not commit2:
            return

        return self._hist_command_runner.run_foreground(['git', 'diff', commit1, commit2])
