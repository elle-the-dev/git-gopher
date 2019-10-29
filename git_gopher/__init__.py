from sys import argv, stdin
from pygments.lexers.diff import DiffLexer
from git_gopher.GitGopher import GitGopher
from git_gopher.CommandFactory import CommandFactory
from git_gopher.Options import Options
from git_gopher.VersionIncrementer import VersionIncrementer
from git_gopher.Fzf import Fzf
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.AddPreview import AddPreview
from git_gopher.Colorize import Colorize

def main():
    git_gopher = GitGopher(CommandFactory(), Options())
    git_gopher.process(argv)

def get_incremented_version():
    print(VersionIncrementer().increment(argv[1], argv[2]))

def add_preview():
    add_preview = AddPreview(GitDataGetter(Fzf()))
    print(add_preview.preview(argv[1]))

def colorize():
    print(Colorize().set_lexer(DiffLexer()).highlight(stdin.read()))
