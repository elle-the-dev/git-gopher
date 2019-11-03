from git_gopher.CommandInterface import CommandInterface

class DifftoolCommitsDirDiff(CommandInterface):
    def __init__(self, hist_command_runer, git_data_getter):
        self._hist_command_runer = hist_command_runer
        self._git_data_getter = git_data_getter

    def run(self):
        commit1 = self._git_data_getter.get_commit_hash(preview='echo "First of two commits to compare."')

        if not commit1:
            return

        commit2 = self._git_data_getter.get_commit_hash(preview='echo "git difftool ' + commit1 + ' {1}"')

        if not commit2:
            return

        self._hist_command_runer.run_foreground(['git', 'difftool', commit1, commit2, '--dir-diff'])
