from git_gopher.CommandInterface import CommandInterface

class DeleteBranchForce(CommandInterface):
    def __init__(self, hist_command_runer, git_data_getter):
        self._hist_command_runer = hist_command_runer
        self._git_data_getter = git_data_getter

    def run(self):
        branches = self._git_data_getter.get_branch_names(preview='echo "git branch -D {2}"')

        if branches:
            for branch in branches:
                self._hist_command_runer.run(['git', 'branch', '-D', branch])
