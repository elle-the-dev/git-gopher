from os import path, getcwd, mkdir
from subprocess import check_output, CalledProcessError, run
from datetime import datetime

class CommandRunner:
    def __init__(self, git_data_getter):
        self._git_data_getter = git_data_getter

    def run(self, cmd: list):
        self._write_history(cmd)
        try:
            return check_output(cmd)
        except CalledProcessError as e:
            return e.output

    def run_foreground(self, cmd: list):
        self._write_history(cmd)
        try:
            return run(cmd)
        except CalledProcessError as e:
            return e.output

    def _write_history(self, cmd: list):
        config_dir = path.expanduser("~") + "/.config/git-gopher"

        if not path.exists(config_dir):
            mkdir(config_dir)

        branch = self._git_data_getter.get_current_branch_name()
        now = datetime.now
        date_str = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())
        cmd_str = ' '.join(cmd)

        with open(config_dir + "/history", "a") as history:
            history.write(date_str + "|" + cmd_str + "|" + branch + getcwd())
