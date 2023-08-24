import unittest
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.CommandRunner import CommandRunner
from git_gopher.DiffCommits import DiffCommits

class TestDiffCommits(unittest.TestCase):

    def test_run(self):
        hash = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_commit_hash = MagicMock(return_value=hash)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run_foreground = MagicMock()
        diff_commits = DiffCommits(command_runner, git_data_getter)
        diff_commits.run()

        command_runner.run_foreground.assert_called_once_with(['git', 'diff', hash, hash])

if __name__ == '__main__':
    unittest.main()
