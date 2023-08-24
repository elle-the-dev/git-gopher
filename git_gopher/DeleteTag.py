from git_gopher.CommandInterface import CommandInterface

class DeleteTag(CommandInterface):
    def __init__(self, hist_command_runer, git_data_getter):
        self._hist_command_runer = hist_command_runer
        self._git_data_getter = git_data_getter

    def run(self):
        tags = self._git_data_getter.get_tag_names(preview='echo "git tag -d {2}"')

        if tags:
            output = ''
            for tag in tags:
                self._hist_command_runer.run(['git', 'tag', '-d', tag])
                output = output + "\nDeleted tag " + tag
            return output
