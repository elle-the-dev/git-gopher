import unittest
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.CommandRunner import CommandRunner
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.PushTag import PushTag

class TestPushTag(unittest.TestCase):

    def test_run(self):
        tag = 'v1.0.0'
        remote = 'foo'
        command_runner = CommandRunner()
        git_data_getter = GitDataGetter(Fzf(), command_runner)
        git_data_getter.get_local_tag_name = MagicMock(return_value=tag)
        git_data_getter.get_remote_name = MagicMock(return_value=remote)

        hist_command_runer = HistoryCommandRunner(git_data_getter, command_runner)
        hist_command_runer.run = MagicMock()
        fetch = PushTag(hist_command_runer, git_data_getter)
        fetch.run()

        hist_command_runer.run.assert_called_once_with(['git', 'push', '-u', remote, tag])

if __name__ == '__main__':
    unittest.main()
