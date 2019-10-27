import unittest
from unittest.mock import MagicMock
from git_gud.Fzf import Fzf
from git_gud.GitDataGetter import GitDataGetter
from git_gud.CommandRunner import CommandRunner
from git_gud.MergeTag import MergeTag

class TestMergeTag(unittest.TestCase):

    def test_run(self):
        tag = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_tag_name = MagicMock(return_value=tag)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run = MagicMock()
        merge_tag = MergeTag(command_runner, git_data_getter)
        merge_tag.run()

        command_runner.run.assert_called_once_with(['git', 'merge', tag])

if __name__ == '__main__':
    unittest.main()
