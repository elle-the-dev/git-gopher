from os import path, getcwd, remove
import unittest
from pathlib import Path
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.CommandRunner import CommandRunner
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.AddPreview import AddPreview

class TestAddPreview(unittest.TestCase):

    def test_run(self):
        file_path = getcwd() + '/test/AddPreviewTestFile.py'
        with open(file_path, "w") as file:
            file.write('print("Hello Test")')

        git_data_getter = GitDataGetter(Fzf(), CommandRunner())
        add_preview = AddPreview(git_data_getter)
        colorized = add_preview.preview(file_path)
        remove(file_path)
        self.assertEqual(colorized, 'print(\x1b[33m"Hello Test"\x1b[39;49;00m)\n')

if __name__ == '__main__':
    unittest.main()
