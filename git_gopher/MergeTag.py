from git_gopher.CommandInterface import CommandInterface

class MergeTag(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        tag = self._git_data_getter.get_tag_name(preview='echo "git merge {2}"')

        if tag:
            self._command_runner.run(['git', 'merge', tag])
