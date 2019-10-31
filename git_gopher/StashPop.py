from git_gopher.CommandInterface import CommandInterface

class StashPop(CommandInterface):
    def __init__(self, hist_command_runer, git_data_getter):
        self._hist_command_runer = hist_command_runer
        self._git_data_getter = git_data_getter

    def run(self):
        stash = self._git_data_getter.get_stash_ref(preview='echo "git stash pop {1}"')

        if stash:
            self._hist_command_runer.run(['git', 'stash', 'pop', stash])
