from git_gopher.CommandInterface import CommandInterface
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class BranchBranch(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        from_branch = self._git_data_getter.get_branch_name(preview='echo "git checkout -b [new_branch_name] {2}"')

        if from_branch:
            new_branch_name = self._git_data_getter.get_branch_name_from_input()
            return self._hist_command_runner.run(['git', 'checkout', '-b', new_branch_name, from_branch])
