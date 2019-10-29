from git_gopher.CommandInterface import CommandInterface

class DeleteBranch(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        branches = self._git_data_getter.get_branch_names(preview='echo "git branch -d {2}"')

        if branches:
            for branch in branches:
                self._command_runner.run(['git', 'branch', '-d', branch])
