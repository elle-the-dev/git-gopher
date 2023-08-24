from subprocess import check_output, run, STDOUT

class CommandRunner:
    def check_output(self, cmd: list, input=None):
        return check_output(cmd, input=input, stderr=STDOUT).decode()

    def run(self, cmd: list):
        return run(cmd)
