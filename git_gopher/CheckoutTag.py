from git_gopher.CommandInterface import CommandInterface
from git_gopher.NoTagsException import NoTagsException
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class CheckoutTag(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        try:
            tag = self._git_data_getter.get_tag_name(preview='echo "git checkout {2}"')
        except NoTagsException:
            print("No tags exist for this repository")
            return

        if tag:
            return self._hist_command_runner.run(['git', 'checkout', tag])
