from subprocess import check_output, run

class CommandRunner:
    def check_output(self, cmd: list, input=None):
        return check_output(cmd, input=input)

    def run(self, cmd: list):
        return run(cmd)
