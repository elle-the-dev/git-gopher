from git_gopher.CommandInterface import CommandInterface
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class DeleteBranch(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        branches = self._git_data_getter.get_branch_names(preview='echo "git branch -d {2}"')

        if branches:
            output = ""
            for branch in branches:
                response = self._hist_command_runner.run(['git', 'branch', '-d', branch])
                if 'not fully merged' in response:
                    output += self.confirm_force_delete(branch)
                else:
                    output += response

    def confirm_force_delete(self, branch):
        yesOrNo = None
        while True:
            yesOrNo = self._git_data_getter.get_confirm_force_delete(branch)
            if yesOrNo == 'y':
                return self._hist_command_runner.run(['git', 'branch', '-D', branch])
            elif yesOrNo == 'n':
                return ''
