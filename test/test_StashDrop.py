import unittest
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.CommandRunner import CommandRunner
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.StashDrop import StashDrop

class TestStashDrop(unittest.TestCase):

    def test_run(self):
        stash = 'foo'
        command_runner = CommandRunner()
        git_data_getter = GitDataGetter(Fzf(), command_runner)
        git_data_getter.get_stash_ref = MagicMock(return_value=stash)

        hist_command_runer = HistoryCommandRunner(git_data_getter, command_runner)
        hist_command_runer.run = MagicMock()
        stash_drop = StashDrop(hist_command_runer, git_data_getter)
        stash_drop.run()

        hist_command_runer.run.assert_called_once_with(['git', 'stash', 'drop', stash])

if __name__ == '__main__':
    unittest.main()
