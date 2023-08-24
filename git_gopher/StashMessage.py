from git_gopher.CommandInterface import CommandInterface

class StashMessage(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        print('git stash push -m "[your message here]"')
        stash_message = self._git_data_getter.get_stash_message_from_input()

        if stash_message:
            self._command_runner.run(['git', 'stash', 'push', '-m', stash_message])
