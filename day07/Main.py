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
times = {}
result = ""
workers = [".", ".", ".", ".", "."]
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']

abc = [x.upper() for x in abc]

for i, x in enumerate(abc):
    times[x] = 60 + i + 1

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
    l.sort()
    ccs = []
    for x in l:
        if len(predecessors[x]) == 0:
            ccs.append(x)
            break

    if len(ccs) == 0:
        print("CC none")
        exit()

    rccs = ccs
    for worker in workers:
        pass

    for key, value in predecessors.items():
        for cc in rccs:
            if cc in value:
                value.remove(cc)

    for cc in rccs:
        result += cc

    for cc in rccs:
        if cc not in used and cc in successors.keys():
            for c in successors[cc]:
                if c not in added:
                    l.append(c)
                    added.add(c)

    for cc in rccs:
        used.add(cc)
        l.remove(cc)

print(result)
