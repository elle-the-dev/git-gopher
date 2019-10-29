from os.path import isfile
from pathlib import Path
from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import TerminalFormatter
from colorama import Fore, Style
import shutil

class StashPreview:
    def __init__(self, git_data_getter):
        self._git_data_getter = git_data_getter

    def preview(self, stash_ref):
        formatter = TerminalFormatter()
        stash_contents = self._git_data_getter.get_stash_contents(stash_ref)

        if isfile(file_path):
            if self._git_data_getter.get_is_tracked(file_path):
                diff = self._git_data_getter.get_diff(file_path)
                lexer = guess_lexer(diff)
                return highlight(diff, lexer, formatter)
            else:
                try:
                    file_contents = Path(file_path).read_text()
                except UnicodeDecodeError:
                    return 'Cannot show preview for this file.'

                lexer = guess_lexer(file_contents)
                return highlight(file_contents, lexer, formatter)

        diff = self._git_data_getter.get_diff(file_path)

        if diff:
            lexer = guess_lexer(diff)
            return highlight(diff, lexer, formatter)

        files = self._git_data_getter.get_unstaged_files_from_dir(file_path).splitlines()
        output = ""
        for file in files:
            #output += u'\u2500' * terminal_width
            output += "\n"
            output += self.get_horizontal_line()
            output += Style.RESET_ALL
            output += file
            output += self.get_horizontal_line()
            try:
                file_contents = Path(file).read_text()
                lexer = guess_lexer(file_contents)
                output += highlight(file_contents, lexer, formatter)
            except UnicodeDecodeError:
                output += 'Cannot show preview for this file.'

        return output

    def get_horizontal_line(self):
        terminal_width = shutil.get_terminal_size().columns
        return "\n" + Fore.YELLOW + (u'\u2500' * terminal_width) + Style.RESET_ALL + "\n"
