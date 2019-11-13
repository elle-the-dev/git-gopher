import unittest
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.CommandRunner import CommandRunner
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.DeleteBranchForce import DeleteBranchForce

class TestDeleteBranchForce(unittest.TestCase):

    def test_run(self):
        branch = 'foo'
        branches = [branch]
        command_runner = CommandRunner()
        git_data_getter = GitDataGetter(Fzf(), command_runner)
        git_data_getter.get_branch_names = MagicMock(return_value=branches)

        hist_command_runer = HistoryCommandRunner(git_data_getter, command_runner)
        hist_command_runer.run = MagicMock()
        delete_branch_force = DeleteBranchForce(hist_command_runer, git_data_getter)
        delete_branch_force.run()

        hist_command_runer.run.assert_called_once_with(['git', 'branch', '-D', branch])

if __name__ == '__main__':
    unittest.main()
