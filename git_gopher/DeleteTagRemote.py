from git_gopher.CommandInterface import CommandInterface

class DeleteTagRemote(CommandInterface):
    def __init__(self, hist_command_runer, git_data_getter):
        self._hist_command_runer = hist_command_runer
        self._git_data_getter = git_data_getter

    def run(self):
        remote = self._git_data_getter.get_remote_name(preview='echo "No action is taken until selecting a tag."')

        if not remote:
            return

        tags = self._git_data_getter.get_tag_names_remote(remote, preview='echo "git tag -d {2}"')

        if tags:
            for tag in tags:
                self._hist_command_runer.run(['git', 'tag', '-d', tag])
                self._hist_command_runer.run(['git', 'push', remote, ':refs/tags/' + tag])
