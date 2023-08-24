import unittest
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.CommandRunner import CommandRunner
from git_gopher.CheckoutBranch import CheckoutBranch

class TestCheckoutBranch(unittest.TestCase):

    def test_run(self):
        branch = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_branch_name = MagicMock(return_value=branch)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run = MagicMock()
        checkout_branch = CheckoutBranch(command_runner, git_data_getter)
        checkout_branch.run()

        command_runner.run.assert_called_once_with(['git', 'checkout', branch])

if __name__ == '__main__':
    unittest.main()
