from sys import argv
from gitgud.GitGud import GitGud
from gitgud.CommandFactory import CommandFactory
from gitgud.Options import Options
from gitgud.VersionIncrementer import VersionIncrementer

def main():
    command_factory = CommandFactory()
    options = Options()
    git_gud = GitGud(command_factory, options)
    git_gud.process(argv)

def get_incremented_version():
    print(VersionIncrementer().increment(argv[1], argv[2]))
