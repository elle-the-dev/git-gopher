from gitgud.CommandInterface import CommandInterface

class DeleteTag(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        tag = self._git_data_getter.get_tag_name(preview='echo "git tag -d {2}"')

        if tag:
            self._command_runner.run(['git', 'tag', '-d', tag])
