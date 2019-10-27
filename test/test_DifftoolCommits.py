import unittest
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.CommandRunner import CommandRunner
from git_gopher.DifftoolCommits import DifftoolCommits

class TestDifftoolCommits(unittest.TestCase):

    def test_run(self):
        hash = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_commit_hash = MagicMock(return_value=hash)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run_foreground = MagicMock()
        difftool_commits = DifftoolCommits(command_runner, git_data_getter)
        difftool_commits.run()

        command_runner.run_foreground.assert_called_once_with(['git', 'difftool', hash, hash])

if __name__ == '__main__':
    unittest.main()
