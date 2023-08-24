from git_gopher.CommandInterface import CommandInterface

class Fetch(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        remote = self._git_data_getter.get_remote_name(preview='echo "git fetch {2}"')

        if remote:
            self._command_runner.run(['git', 'fetch', remote])
