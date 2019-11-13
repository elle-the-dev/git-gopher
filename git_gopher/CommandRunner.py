from subprocess import check_output, run, STDOUT
from typing import List

class CommandRunner:
    def check_output(self, cmd: List[str], input: str=None) -> str:
        return check_output(cmd, input=input, stderr=STDOUT).decode()

    def run(self, cmd: List[str]) -> str:
        return run(cmd)
