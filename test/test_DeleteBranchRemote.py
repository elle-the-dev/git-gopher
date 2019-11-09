import unittest
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.CommandRunner import CommandRunner
from git_gopher.DeleteBranchRemote import DeleteBranchRemote

class TestDeleteBranchRemote(unittest.TestCase):

    def test_run(self):
        remote = 'bar'
        branch = 'foo'
        branches = [branch]
        command_runner = CommandRunner()
        git_data_getter = GitDataGetter(Fzf(), command_runner)
        git_data_getter.get_remote_name= MagicMock(return_value=remote)
        git_data_getter.get_branch_names_remote = MagicMock(return_value=branches)
        command_runner.run = MagicMock()
        delete_branch = DeleteBranchRemote(command_runner, git_data_getter)
        delete_branch.run()

        command_runner.run.assert_called_once_with(['git', 'push', remote, '--delete', branch])

if __name__ == '__main__':
    unittest.main()
