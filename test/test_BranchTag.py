import unittest
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.CommandRunner import CommandRunner
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.BranchTag import BranchTag

class TestBranchTag(unittest.TestCase):

    def test_run(self):
        from_tag = 'v1.0.0'
        new_branch_name = 'newfoo'
        command_runner = CommandRunner()
        git_data_getter = GitDataGetter(Fzf(), command_runner)
        git_data_getter.get_tag_name = MagicMock(return_value=from_tag)
        git_data_getter.get_branch_name_from_input = MagicMock(return_value=new_branch_name)

        hist_command_runer = HistoryCommandRunner(git_data_getter, command_runner)
        hist_command_runer.run = MagicMock()
        branch_branch = BranchTag(hist_command_runer, git_data_getter)
        branch_branch.run()

        hist_command_runer.run.assert_called_once_with(['git', 'checkout', '-b', new_branch_name, from_tag])

if __name__ == '__main__':
    unittest.main()
