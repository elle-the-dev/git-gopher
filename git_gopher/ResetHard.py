from git_gopher.CommandInterface import CommandInterface

class ResetHard(CommandInterface):
    def __init__(self, hist_command_runer, git_data_getter):
        self._hist_command_runer = hist_command_runer
        self._git_data_getter = git_data_getter

    def run(self):
        hash = self._git_data_getter.get_commit_hash(preview='echo "git reset --hard {1}"')

        if hash:
            self._hist_command_runer.run(['git', 'reset', '--hard', hash])
