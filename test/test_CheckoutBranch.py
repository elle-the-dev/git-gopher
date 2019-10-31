import unittest
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.CheckoutBranch import CheckoutBranch

class TestCheckoutBranch(unittest.TestCase):

    def test_run(self):
        branch = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_branch_name = MagicMock(return_value=branch)
        hist_command_runer = HistoryCommandRunner(git_data_getter)
        hist_command_runer.run = MagicMock()
        checkout_branch = CheckoutBranch(hist_command_runer, git_data_getter)
        checkout_branch.run()

        hist_command_runer.run.assert_called_once_with(['git', 'checkout', branch])

if __name__ == '__main__':
    unittest.main()
