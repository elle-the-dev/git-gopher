from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import TerminalFormatter

class Colorize:
    def __init__(self):
        self.lexer = None

    def highlight(self, content):
        formatter = TerminalFormatter()

        if self.lexer:
            lexer = self.lexer
        else:
            lexer = guess_lexer(content)

        return highlight(content, lexer, formatter)

    def set_lexer(self, lexer):
        self.lexer = lexer
        return self
