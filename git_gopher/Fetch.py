from git_gopher.CommandInterface import CommandInterface

class Fetch(CommandInterface):
    def __init__(self, hist_command_runer, git_data_getter):
        self._hist_command_runer = hist_command_runer
        self._git_data_getter = git_data_getter

    def run(self):
        remote = self._git_data_getter.get_remote_name(preview='echo "git fetch {2}"')

        if remote:
            self._hist_command_runer.run(['git', 'fetch', remote])
