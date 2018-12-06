from copy import deepcopy

import InputHelper as iH

iH = iH.InputHelper(5)
lines = iH.lines
numbers = iH.numbers

line = list(lines[0])
print(line)
found = True

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']


best = 20000
winner = 'a'

for l in abc:
    nline = deepcopy(line)
    nline = [x for x in nline if x != l]
    nline = [x for x in nline if x != l.capitalize()]
    found = True
    while found:
        found = False
        for i, c in enumerate(nline):
            if i + 1 < len(nline):
                if ord(nline[i + 1]) != ord(str(c)):
                    if ord(nline[i + 1]) == ord(str(c).capitalize()) or ord(nline[i + 1]) == ord(str(c).lower()):
                        del (nline[i])
                        del (nline[i])
                        found = True

    if len(nline) < best:

        best = len(nline)
        winner = l


print(best, winner)
