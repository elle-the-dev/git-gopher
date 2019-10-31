import unittest
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.MergeTag import MergeTag

class TestMergeTag(unittest.TestCase):

    def test_run(self):
        tag = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_tag_name = MagicMock(return_value=tag)
        hist_command_runer = HistoryCommandRunner(git_data_getter)
        hist_command_runer.run = MagicMock()
        merge_tag = MergeTag(hist_command_runer, git_data_getter)
        merge_tag.run()

        hist_command_runer.run.assert_called_once_with(['git', 'merge', tag])

if __name__ == '__main__':
    unittest.main()
