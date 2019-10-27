from git_gopher.CommandInterface import CommandInterface

class CherryPick(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        branch = self._git_data_getter.get_branch_name(preview='echo "Select a branch. No action is taken until selecting a commit."')

        if not branch:
            return

        hash = self._git_data_getter.get_commit_hash(branch=branch, preview='echo "git cherry-pick -e {1}"')

        if not hash:
            return

        self._command_runner.run(['git', 'cherry-pick', '-e', hash])
