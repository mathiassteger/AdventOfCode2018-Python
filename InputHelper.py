import os


class InputHelper:
    def __init__(self, dayNr):
        self.dayNr = dayNr

    def lines(self, do_strip=False):
        os.chdir('..')
        f = open('input' + str(self.dayNr) + '.txt', 'r')

        lines = f.readlines()

        if do_strip:
            lines = [x.strip() for x in lines]

        f.close()

        return lines
