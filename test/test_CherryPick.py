import unittest
from unittest.mock import MagicMock
from gitgud.Fzf import Fzf
from gitgud.GitDataGetter import GitDataGetter
from gitgud.CommandRunner import CommandRunner
from gitgud.CherryPick import CherryPick

class TestCherryPick(unittest.TestCase):

    def test_run(self):
        branch = 'foo'
        hash = 'bash'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_branch_name = MagicMock(return_value=branch)
        git_data_getter.get_commit_hash = MagicMock(return_value=hash)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run = MagicMock()
        cherry_pick = CherryPick(command_runner, git_data_getter)
        cherry_pick.run()

        command_runner.run.assert_called_once_with(['git', 'cherry-pick', '-e', hash])

if __name__ == '__main__':
    unittest.main()
