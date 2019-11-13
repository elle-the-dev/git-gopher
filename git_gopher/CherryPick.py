from git_gopher.CommandInterface import CommandInterface
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class CherryPick(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        branch = self._git_data_getter.get_branch_name(preview='echo "Select a branch. No action is taken until selecting a commit."')

        if not branch:
            return

        hash = self._git_data_getter.get_commit_hash(branch=branch, preview='echo "git cherry-pick -e {1}"')

        if not hash:
            return

        return self._hist_command_runner.run(['git', 'cherry-pick', '-e', hash])
