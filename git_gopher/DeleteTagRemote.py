from git_gopher.CommandInterface import CommandInterface
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class DeleteTagRemote(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        remote = self._git_data_getter.get_remote_name(preview='echo "No action is taken until selecting a tag."')

        if not remote:
            return

        tags = self._git_data_getter.get_tag_names_remote(remote, preview='echo "git tag -d {2} && git push "' + remote + ' {2}"')

        if tags:
            output = ''
            for tag in tags:
                self._hist_command_runner.run(['git', 'tag', '-d', tag])
                self._hist_command_runner.run(['git', 'push', '--delete', remote, tag])
                output = output + "\nDeleted tag " + tag + " on " + remote
            return output
