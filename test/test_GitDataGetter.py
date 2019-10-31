import unittest
from unittest.mock import patch, MagicMock
from subprocess import check_output, CalledProcessError
from git_gopher.Fzf import Fzf
from git_gopher.CommandRunner import CommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class TestGitDataGetter(unittest.TestCase):

    def test_get_current_branch_name(self):
        branch = b'foo'
        command_runner = CommandRunner()
        command_runner.check_output = MagicMock(return_value=branch)

        git_data_getter = git_data_getter = GitDataGetter(Fzf(), command_runner)
        result = git_data_getter.get_current_branch_name()

        self.assertEqual(result, 'foo')
        command_runner.check_output.assert_called_once_with(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])

    def test_get_branch_name(self):
        branch = 'foo'
        command_runner = CommandRunner()
        command_runner.check_output = MagicMock(return_value=b"branch | bar")
        fzf = Fzf()
        fzf.run = MagicMock(return_value="branch\t" + branch)

        git_data_getter = git_data_getter = GitDataGetter(fzf, command_runner)
        result = git_data_getter.get_branch_name()
        self.assertEqual(result, branch)

if __name__ == '__main__':
    unittest.main()
