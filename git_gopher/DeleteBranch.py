from git_gopher.CommandInterface import CommandInterface

class DeleteBranch(CommandInterface):
    def __init__(self, hist_command_runer, git_data_getter):
        self._hist_command_runer = hist_command_runer
        self._git_data_getter = git_data_getter

    def run(self):
        branches = self._git_data_getter.get_branch_names(preview='echo "git branch -d {2}"')

        if branches:
            for branch in branches:
                response = self._hist_command_runer.run(['git', 'branch', '-d', branch]).decode()
                if 'not fully merged' in response:
                    self.confirm_force_delete(branch)

    def confirm_force_delete(self, branch):
        yesOrNo = None
        while True:
            yesOrNo = self._git_data_getter.get_confirm_force_delete(branch)
            if yesOrNo == 'y':
                self._hist_command_runer.run(['git', 'branch', '-D', branch])
                break
            elif yesOrNo == 'n':
                break
