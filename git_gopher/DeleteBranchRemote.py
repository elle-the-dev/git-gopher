from git_gopher.CommandInterface import CommandInterface
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class DeleteBranchRemote(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        remote = self._git_data_getter.get_remote_name(preview='echo "Select a remote. No action is taken until selecting a branch."')

        if not remote:
            return

        branches = self._git_data_getter.get_branch_names_remote(remote, preview='echo "git branch -d {2}"')

        if branches:
            output = ""
            for branch in branches:
                output += self._hist_command_runner.run(['git', 'push', remote, '--delete', branch])
            return output
