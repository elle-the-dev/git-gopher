import unittest
from unittest.mock import MagicMock
from gitgud.Fzf import Fzf
from gitgud.GitDataGetter import GitDataGetter
from gitgud.CommandRunner import CommandRunner
from gitgud.Reset import Reset

class TestReset(unittest.TestCase):

    def test_run(self):
        hash = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_commit_hash = MagicMock(return_value=hash)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run = MagicMock()
        reset = Reset(command_runner, git_data_getter)
        reset.run()

        command_runner.run.assert_called_once_with(['git', 'reset', hash])

if __name__ == '__main__':
    unittest.main()
