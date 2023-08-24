import unittest
from unittest.mock import MagicMock, call
from git_gopher.Fzf import Fzf
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.CommandRunner import CommandRunner
from git_gopher.DeleteTagRemote import DeleteTagRemote

class TestDeleteTagRemote(unittest.TestCase):

    def test_run(self):
        remote = 'foo'
        tag = 'v1.0.0'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_remote_name = MagicMock(return_value=remote)
        git_data_getter.get_tag_name_remote = MagicMock(return_value=tag)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run = MagicMock()
        delete_tag_remote = DeleteTagRemote(command_runner, git_data_getter)
        delete_tag_remote.run()

        calls = [call(['git', 'tag', '-d', tag]), call(['git', 'push', remote, ':refs/tags/' + tag])]
        command_runner.run.assert_has_calls(calls)

if __name__ == '__main__':
    unittest.main()
