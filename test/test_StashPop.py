import unittest
from unittest.mock import MagicMock
from gitgud.Fzf import Fzf
from gitgud.GitDataGetter import GitDataGetter
from gitgud.CommandRunner import CommandRunner
from gitgud.StashPop import StashPop

class TestStashPop(unittest.TestCase):

    def test_run(self):
        stash = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_stash_ref = MagicMock(return_value=stash)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run = MagicMock()
        stash_pop = StashPop(command_runner, git_data_getter)
        stash_pop.run()

        command_runner.run.assert_called_once_with(['git', 'stash', 'pop', stash])

if __name__ == '__main__':
    unittest.main()
