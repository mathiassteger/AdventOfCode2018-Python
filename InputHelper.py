import os
import re


class InputHelper:
    def __init__(self, day_nr):
        self.dayNr = day_nr
        self.lines = self.make_lines(do_strip=True)
        self.numbers = self.get_all_numbers(self.lines)

    def make_lines(self, do_strip=False):
        os.chdir('..')
        f = open('input' + str(self.dayNr) + '.txt', 'r')

        lines = f.readlines()

        if do_strip:
            lines = [x.strip() for x in lines]

        f.close()

        return lines

    def get_all_numbers(self, lines):
        numbers = map(lambda s: map(int, re.findall(r'-?\d+', s)), lines)
        return [list(x) for x in numbers]
