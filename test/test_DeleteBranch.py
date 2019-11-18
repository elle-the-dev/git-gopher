import unittest
from unittest.mock import MagicMock, call
from git_gopher.Fzf import Fzf
from git_gopher.CommandRunner import CommandRunner
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.DeleteBranch import DeleteBranch

class TestDeleteBranch(unittest.TestCase):

    def test_run(self):
        branch = 'foo'
        branches = [branch]
        command_runner = CommandRunner()
        git_data_getter = GitDataGetter(Fzf(), command_runner)
        git_data_getter.get_branch_names = MagicMock(return_value=branches)

        hist_command_runer = HistoryCommandRunner(git_data_getter, command_runner)
        hist_command_runer.run = MagicMock()
        delete_branch = DeleteBranch(hist_command_runer, git_data_getter)
        delete_branch.run()

        hist_command_runer.run.assert_called_once_with(['git', 'branch', '-d', branch])

    def test_force_delete_yes(self):
        branch = 'foo'
        branches = [branch]
        command_runner = CommandRunner()
        git_data_getter = GitDataGetter(Fzf(), command_runner)
        git_data_getter.get_branch_names = MagicMock(return_value=branches)
        git_data_getter.get_confirm_force_delete = MagicMock(return_value="y")

        hist_command_runer = HistoryCommandRunner(git_data_getter, command_runner)
        hist_command_runer.run = MagicMock(return_value="error: not fully merged")
        delete_branch = DeleteBranch(hist_command_runer, git_data_getter)
        delete_branch.run()

        calls = [call(['git', 'branch', '-d', branch]), call(['git', 'branch', '-D', branch])]
        hist_command_runer.run.assert_has_calls(calls)

    def test_force_delete_no(self):
        branch = 'foo'
        branches = [branch]
        command_runner = CommandRunner()
        git_data_getter = GitDataGetter(Fzf(), command_runner)
        git_data_getter.get_branch_names = MagicMock(return_value=branches)
        git_data_getter.get_confirm_force_delete = MagicMock(return_value="n")

        hist_command_runer = HistoryCommandRunner(git_data_getter, command_runner)
        hist_command_runer.run = MagicMock(return_value="error: not fully merged")
        delete_branch = DeleteBranch(hist_command_runer, git_data_getter)
        delete_branch.run()

if __name__ == '__main__':
    unittest.main()
