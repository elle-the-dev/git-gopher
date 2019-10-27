from git_gopher.CommandInterface import CommandInterface

class StashPop(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        stash = self._git_data_getter.get_stash_ref(preview='echo "git stash pop {1}"')

        if stash:
            self._command_runner.run(['git', 'stash', 'pop', stash])
