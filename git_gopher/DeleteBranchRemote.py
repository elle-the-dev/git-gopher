from git_gopher.CommandInterface import CommandInterface

class DeleteBranchRemote(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        remote = self._git_data_getter.get_remote_name(preview='echo "Select a remote. No action is taken until selecting a branch."')

        if not remote:
            return

        branches = self._git_data_getter.get_branch_names_remote(remote, preview='echo "git branch -d {2}"')

        if branches:
            output = ""
            for branch in branches:
                output += self._command_runner.run(['git', 'push', remote, '--delete', branch])
            return output
