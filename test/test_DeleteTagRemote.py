import unittest
from unittest.mock import MagicMock, call
from git_gopher.Fzf import Fzf
from git_gopher.CommandRunner import CommandRunner
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.DeleteTagRemote import DeleteTagRemote

class TestDeleteTagRemote(unittest.TestCase):

    def test_run(self):
        remote = 'foo'
        tag = 'refs/tags/v1.0.0'
        tags = [tag]
        command_runner = CommandRunner()
        git_data_getter = GitDataGetter(Fzf(), command_runner)
        git_data_getter.get_remote_name = MagicMock(return_value=remote)
        git_data_getter.get_tag_names_remote = MagicMock(return_value=tags)

        hist_command_runer = HistoryCommandRunner(git_data_getter, command_runner)
        hist_command_runer.run = MagicMock()
        delete_tag_remote = DeleteTagRemote(hist_command_runer, git_data_getter)
        delete_tag_remote.run()

        calls = [call(['git', 'tag', '-d', tag]), call(['git', 'push', '--delete', remote, tag])]
        hist_command_runer.run.assert_has_calls(calls)

if __name__ == '__main__':
    unittest.main()
