from git_gopher.CommandInterface import CommandInterface

class Reset(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        hash = self._git_data_getter.get_commit_hash(preview='echo "git reset {1}"')

        if hash:
            self._command_runner.run(['git', 'reset', hash])
