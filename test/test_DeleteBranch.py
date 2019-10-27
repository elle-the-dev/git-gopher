import unittest
from unittest.mock import MagicMock
from gitgud.Fzf import Fzf
from gitgud.GitDataGetter import GitDataGetter
from gitgud.CommandRunner import CommandRunner
from gitgud.DeleteBranch import DeleteBranch

class TestDeleteBranch(unittest.TestCase):

    def test_run(self):
        branch = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_branch_name = MagicMock(return_value=branch)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run = MagicMock()
        delete_branch = DeleteBranch(command_runner, git_data_getter)
        delete_branch.run()

        command_runner.run.assert_called_once_with(['git', 'branch', '-d', branch])

if __name__ == '__main__':
    unittest.main()
