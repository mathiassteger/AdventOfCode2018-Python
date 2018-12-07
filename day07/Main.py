import InputHelper as iH

iH = iH.InputHelper(0)
lines = iH.lines
numbers = iH.numbers

successors = {}
predecessors = {}
l = []
used = set()
added = set()
letters = set()
result = ""

for line in lines:
    current = line.split()[1]
    follower = line.split()[7]
    letters.add(current)
    letters.add(follower)

    if current in successors:
        successors[current].append(follower)
    else:
        successors[current] = [follower]

    if follower in predecessors:
        predecessors[follower].append(current)
    else:
        predecessors[follower] = [current]


for x in letters:
    if x not in predecessors.keys():
        predecessors[x] = []
        l.append(x)

while len(l) > 0:
    print("List:", l)
    l.sort()
    cc = None
    for x in l:
        print(x, predecessors[x])
        if len(predecessors[x]) == 0:
            cc = x
            break


    if cc == None:
        print("CC none")
        exit()

    print("CC:", cc)
    for key, value in predecessors.items():
        if cc in value:
            value.remove(cc)

    result += cc

    if cc not in used and cc in successors.keys():
        for c in successors[cc]:
            if c not in added:
                l.append(c)
                added.add(c)

    start = cc
    used.add(start)
    l.remove(cc)

print(result)  # FQUSZRPOTYONMKIIHGCBWC
