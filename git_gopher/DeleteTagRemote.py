from git_gopher.CommandInterface import CommandInterface

class DeleteTagRemote(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        remote = self._git_data_getter.get_remote_name(preview='echo "No action is taken until selecting a tag."')

        if not remote:
            return

        tag = self._git_data_getter.get_tag_name_remote(remote, preview='echo "git tag -d {2}"')

        if tag:
            self._command_runner.run(['git', 'tag', '-d', tag])
            self._command_runner.run(['git', 'push', remote, ':refs/tags/' + tag])
