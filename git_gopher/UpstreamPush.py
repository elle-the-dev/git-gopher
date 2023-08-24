from git_gopher.CommandInterface import CommandInterface

class UpstreamPush(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        branch = self._git_data_getter.get_current_branch_name()
        preview = 'echo "git push -u {2} ' + branch + '"'
        remote = self._git_data_getter.get_remote_name(preview=preview)

        if remote:
            self._command_runner.run(['git', 'push', '-u', remote, branch])