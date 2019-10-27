from git_gopher.CommandInterface import CommandInterface
from git_gopher.NoTagsException import NoTagsException

class CheckoutTag(CommandInterface):
    def __init__(self, command_runner, git_data_getter):
        self._command_runner = command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        try:
            tag = self._git_data_getter.get_tag_name(preview='echo "git checkout {2}"')
        except NoTagsException:
            print("No tags exist for this repository")
            return

        if tag:
            self._command_runner.run(['git', 'checkout', tag])
