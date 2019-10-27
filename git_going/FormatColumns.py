import csv
from re import sub
from colorama import Fore, Style

class FormatColumns:
    _colors: dict = {}

    def format(self, data: str, colors: list=[]) -> str:
        data = self.__remove_blank_lines(data)
        table = [list(map(str.strip, row.split('|'))) for row in data.strip().split("\n")]
        max_column_lengths = [max(len(str(cell)) for cell in line) for line in zip(*table)]

        out: str = ""
        for row in table:
            line = ""
            for i in range(len(max_column_lengths)):
                col = "{: <"+str(max_column_lengths[i])+"}"
                if (i in self._colors):
                    col = self._colors[i] + col + Style.RESET_ALL
                line += col + "\t"
            out += line.format(*row).strip()+"\n"

        return out

    def set_colors(self, colors: dict) -> 'FormatColumns':
        self._colors = colors
        return self

    def __remove_blank_lines(self, string: str) -> str:
        return sub(r'(?m)^\n?', '', ''.join(string))
