from subprocess import check_output, run

class CommandRunner:
    def check_output(self, cmd: list):
        return check_output(cmd)

    def run(self, cmd: list):
        return run(cmd)
