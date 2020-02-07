from os import path
from git_gopher.CommandInterface import CommandInterface
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class CheckoutBranchRemote(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        DIR = path.dirname(path.realpath(__file__))
        branch = self._git_data_getter.get_branch_name(options=['--all'], preview='ggo-checkout-branch-remote-preview {2}')

        if not branch:
            return

        cmd = self._git_data_getter.checkout_branch_remote_command(branch)
        return self._hist_command_runner.run(cmd)
