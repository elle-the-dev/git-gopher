from git_gopher.CommandInterface import CommandInterface
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class DeleteTag(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        tags = self._git_data_getter.get_tag_names(preview='echo "git tag -d {2}"')

        if tags:
            output = ''
            for tag in tags:
                self._hist_command_runner.run(['git', 'tag', '-d', tag])
                output = output + "\nDeleted tag " + tag
            return output
