from git_gopher.CommandInterface import CommandInterface
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.VersionIncrementer import VersionIncrementer

class TagIncrementVersion(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter, version_incrementer: VersionIncrementer):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter
        self._version_incrementer = version_incrementer

    def run(self):
        most_recent_tag = self._git_data_getter.get_most_recent_tag()
        preview = 'echo "git tag $(ggo-get-incremented-version ' + most_recent_tag + ' {2})"'
        semantic_part = self._git_data_getter.get_semantic_part(preview=preview)
        new_version = self._version_incrementer.increment(most_recent_tag, semantic_part)
        return self._hist_command_runner.run(['git', 'tag', new_version])
