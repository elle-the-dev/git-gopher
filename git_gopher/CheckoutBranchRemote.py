from os import path
from git_gopher.CommandInterface import CommandInterface

class CheckoutBranchRemote(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        DIR = path.dirname(path.realpath(__file__))
        branch = self._git_data_getter.get_branch_name(options=['--all'], preview=DIR+'/_checkout-branch-remote-command {2}')

        if not branch:
            return

        cmd = self._git_data_getter.checkout_branch_remote_command(branch)
        self._command_runner.run(cmd)
