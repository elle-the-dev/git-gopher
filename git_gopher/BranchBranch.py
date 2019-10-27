from git_gopher.CommandInterface import CommandInterface

class BranchBranch(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        from_branch = self._git_data_getter.get_branch_name(preview='echo "git checkout -b [new_branch_name] {2}"')

        if from_branch:
            new_branch_name = self._git_data_getter.get_branch_name_from_input()
            self._command_runner.run(['git', 'checkout', '-b', new_branch_name, from_branch])
