from git_gopher.CommandInterface import CommandInterface

class DeleteBranchForce(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        branch = self._git_data_getter.get_branch_name(preview='echo "git branch -D {2}"')

        if branch:
            self._command_runner.run(['git', 'branch', '-D', branch])
