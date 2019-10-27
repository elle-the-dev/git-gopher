import unittest
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.CommandRunner import CommandRunner
from git_gopher.BranchBranch import BranchBranch

class TestBranchBranch(unittest.TestCase):

    def test_run(self):
        from_branch = 'foo'
        new_branch_name = 'newfoo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_branch_name = MagicMock(return_value=from_branch)
        git_data_getter.get_branch_name_from_input = MagicMock(return_value=new_branch_name)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run = MagicMock()
        branch_branch = BranchBranch(command_runner, git_data_getter)
        branch_branch.run()

        command_runner.run.assert_called_once_with(['git', 'checkout', '-b', new_branch_name, from_branch])

if __name__ == '__main__':
    unittest.main()
