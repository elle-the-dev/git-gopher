from sys import argv
from git_gopher.GitGopher import GitGopher
from git_gopher.CommandFactory import CommandFactory
from git_gopher.Options import Options
from git_gopher.VersionIncrementer import VersionIncrementer

def main():
    git_gopher = GitGopher(CommandFactory(), Options())
    git_gopher.process(argv)

def get_incremented_version():
    print(VersionIncrementer().increment(argv[1], argv[2]))
