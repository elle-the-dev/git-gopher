import unittest
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.DeleteBranch import DeleteBranch

class TestDeleteBranch(unittest.TestCase):

    def test_run(self):
        branch = 'foo'
        branches = [branch]
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_branch_names = MagicMock(return_value=branches)
        hist_command_runer = HistoryCommandRunner(git_data_getter)
        hist_command_runer.run = MagicMock()
        delete_branch = DeleteBranch(hist_command_runer, git_data_getter)
        delete_branch.run()

        hist_command_runer.run.assert_called_once_with(['git', 'branch', '-d', branch])

if __name__ == '__main__':
    unittest.main()
