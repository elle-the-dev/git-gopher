from sys import argv
from git_going.GitGoing import GitGoing
from git_going.CommandFactory import CommandFactory
from git_going.Options import Options
from git_going.VersionIncrementer import VersionIncrementer

def main():
    command_factory = CommandFactory()
    options = Options()
    git_going = GitGoing(command_factory, options)
    git_going.process(argv)

def get_incremented_version():
    print(VersionIncrementer().increment(argv[1], argv[2]))
