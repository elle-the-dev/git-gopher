import unittest
from unittest.mock import patch, MagicMock
from subprocess import check_output, CalledProcessError
from git_gopher.Fzf import Fzf
from git_gopher.CommandRunner import CommandRunner
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.NoTagsException import NoTagsException

class TestGitDataGetter(unittest.TestCase):

    def test_get_current_branch_name(self):
        branch = 'foo'
        command_runner = CommandRunner()
        command_runner.check_output = MagicMock(return_value=branch)

        git_data_getter = GitDataGetter(Fzf(), command_runner)
        result = git_data_getter.get_current_branch_name()

        self.assertEqual(result, 'foo')
        command_runner.check_output.assert_called_once_with(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])

    def test_get_branch_name(self):
        branch = 'foo'
        command_runner = CommandRunner()
        command_runner.check_output = MagicMock(return_value="branch | bar")
        fzf = Fzf()
        fzf.run = MagicMock(return_value="branch\t" + branch)

        git_data_getter = GitDataGetter(fzf, command_runner)
        result = git_data_getter.get_branch_name()
        self.assertEqual(result, branch)

    def test_get_tag_name_from_tags(self):
        tag = 'foo'
        command_runner = CommandRunner()
        command_runner.check_output = MagicMock(return_value="tag | bar")
        fzf = Fzf()
        fzf.run = MagicMock(return_value="tag\t" + tag)

        git_data_getter = GitDataGetter(fzf, command_runner)
        result = git_data_getter.get_tag_name()
        self.assertEqual(result, tag)

    def test_get_tag_name_from_tags_throws_exception_on_no_tags(self):
        tag = 'foo'
        command_runner = CommandRunner()
        command_runner.check_output = MagicMock(return_value="")
        fzf = Fzf()
        fzf.run = MagicMock(return_value="tag\t" + tag)

        git_data_getter = GitDataGetter(fzf, command_runner)
        self.assertRaises(NoTagsException, git_data_getter.get_tag_name)

    def test_get_commit_hash(self):
        branch = 'foo'
        commit = 'afe786e5'
        output = commit + '\t1 day ago\tFoo Bar\tSomething something commit'
        command_runner = CommandRunner()
        command_runner.check_output = MagicMock(return_value='')
        fzf = Fzf()
        fzf.run = MagicMock(return_value=output)

        git_data_getter = GitDataGetter(fzf, command_runner)
        result = git_data_getter.get_commit_hash(branch)
        self.assertEqual(result, commit)

if __name__ == '__main__':
    unittest.main()
