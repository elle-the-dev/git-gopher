import unittest
from unittest.mock import MagicMock
from git_gud.Fzf import Fzf
from git_gud.GitDataGetter import GitDataGetter
from git_gud.CommandRunner import CommandRunner
from git_gud.StashApply import StashApply

class TestStashApply(unittest.TestCase):

    def test_run(self):
        stash = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_stash_ref = MagicMock(return_value=stash)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run = MagicMock()
        stash_apply = StashApply(command_runner, git_data_getter)
        stash_apply.run()

        command_runner.run.assert_called_once_with(['git', 'stash', 'apply', stash])

if __name__ == '__main__':
    unittest.main()
