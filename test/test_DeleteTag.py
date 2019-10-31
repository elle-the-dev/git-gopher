import unittest
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.DeleteTag import DeleteTag

class TestDeleteTag(unittest.TestCase):

    def test_run(self):
        tag = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_tag_name = MagicMock(return_value=tag)
        hist_command_runer = HistoryCommandRunner(git_data_getter)
        hist_command_runer.run = MagicMock()
        delete_tag = DeleteTag(hist_command_runer, git_data_getter)
        delete_tag.run()

        hist_command_runer.run.assert_called_once_with(['git', 'tag', '-d', tag])

if __name__ == '__main__':
    unittest.main()
