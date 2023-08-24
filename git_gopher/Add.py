from os import path
from colorama import Fore, Style
from git_gopher.CommandInterface import CommandInterface
from git_gopher.FormatColumns import FormatColumns

class Add(CommandInterface):
    def __init__(self, command_runner, git_data_getter, fzf):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter
        self._fzf = fzf

    def run(self):
        unstaged_files = self._get_unstaged_files()
        filepath = self._get_user_selection(unstaged_files)

        if filepath:
            self._command_runner.run(['git', 'add', filepath])

    def _get_unstaged_files(self):
        unstaged_files = self._git_data_getter.get_unstaged_files().splitlines()

        # break up path into subdirectories
        # e.g. path/to/file becomes path\nto
        # so we can include directories in the list to add
        for file in unstaged_files:
            for dir in path.dirname(file).split('/'):
                if path.isdir(dir):
                    dir_files = self._git_data_getter.get_unstaged_files_from_dir(dir)
                    # if there's only 1 file under the given directory, we
                    # don't need to subdivide further, as choosing a parent
                    # directory is the same as choosing the file itself

                    if len(dir_files.splitlines()) > 1:
                        unstaged_files.append(dir)
                    else:
                        break

        # list only unique folders as the above subdirs don't consider it
        unstaged_files = list(set(unstaged_files))
        unstaged_files.sort()

        return self._colorize_unstaged_files(unstaged_files)

    def _colorize_unstaged_files(self, unstaged_files):
        for i in range(len(unstaged_files)):
            file = unstaged_files[i]

            if not self._git_data_getter.get_is_tracked(file):
                file = Fore.RED + file

            if path.isdir(unstaged_files[i]):
                unstaged_files[i] = Fore.BLUE + "dir" + Style.RESET_ALL + " | " + file
            else:
                unstaged_files[i] = Fore.CYAN + "file" + Style.RESET_ALL + " | " + file

        return unstaged_files

    def _get_user_selection(self, unstaged_files):
        format_columns = FormatColumns()
        DIR = path.dirname(path.realpath(__file__))
        preview = DIR + "/_add-preview {2}"
        filepath = self._fzf.run(format_columns.set_colors({0: Fore.BLUE}).format('\n'.join(unstaged_files)), preview=preview, preview_window="--preview-window=right")

        if (filepath):
            return filepath.split('\t')[1].strip()
