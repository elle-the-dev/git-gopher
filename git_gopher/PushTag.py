from git_gopher.CommandInterface import CommandInterface

class PushTag(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        preview = 'echo "Select a remote. No action is taken until selecting a tag."'
        remote = self._git_data_getter.get_remote_name(preview=preview)

        if not remote:
            return

        tag = self._git_data_getter.get_local_tag_name(remote, preview='echo "git push -u ' + remote + ' {2}"')
        print(tag)

        if tag:
            self._command_runner.run(['git', 'push', '-u', remote, tag])
