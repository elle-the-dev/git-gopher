import unittest
from unittest.mock import MagicMock
from git_gud.Fzf import Fzf
from git_gud.GitDataGetter import GitDataGetter
from git_gud.CommandRunner import CommandRunner
from git_gud.StashMessage import StashMessage

class TestStashMessage(unittest.TestCase):

    def test_run(self):
        message = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_stash_message_from_input = MagicMock(return_value=message)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run = MagicMock()
        stash_message = StashMessage(command_runner, git_data_getter)
        stash_message.run()

        command_runner.run.assert_called_once_with(['git', 'stash', 'push', '-m', message])

if __name__ == '__main__':
    unittest.main()
