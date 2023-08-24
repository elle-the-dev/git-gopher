import unittest
from unittest.mock import MagicMock
from gitgud.Fzf import Fzf
from gitgud.GitDataGetter import GitDataGetter
from gitgud.CommandRunner import CommandRunner
from gitgud.CheckoutBranchRemote import CheckoutBranchRemote

class TestCheckoutBranchRemote(unittest.TestCase):

    def test_run(self):
        branch = 'foo'
        remote_command = ['git', 'checkout', '--track', branch]
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_branch_name = MagicMock(return_value=branch)
        git_data_getter.checkout_branch_remote_command = MagicMock(return_value=remote_command)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run = MagicMock()
        checkout_branch = CheckoutBranchRemote(command_runner, git_data_getter)
        checkout_branch.run()

        command_runner.run.assert_called_once_with(remote_command)

if __name__ == '__main__':
    unittest.main()
