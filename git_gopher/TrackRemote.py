from git_gopher.CommandInterface import CommandInterface

class TrackRemote(CommandInterface):
    def __init__(self, hist_command_runer, git_data_getter):
        self._hist_command_runer = hist_command_runer
        self._git_data_getter = git_data_getter

    def run(self):
        branch = self._git_data_getter.get_current_branch_name()
        preview = 'echo "git branch ' + branch + ' -u {2}/' + branch + '" | sed -e s/"\'"//g'
        remote = self._git_data_getter.get_remote_name(preview=preview)

        if remote:
            self._hist_command_runer.run(['git', 'branch', branch, '-u', remote + '/' + branch])
