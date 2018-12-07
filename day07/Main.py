import InputHelper as iH

iH = iH.InputHelper(7)
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

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']

abc = [x.upper() for x in abc]

n_workers = 5
base = 60
for i, x in enumerate(abc):
    times[x] = base + i + 1
workers = []
for i in range(n_workers):
    workers.append(".")

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

seconds = 0
l.sort()
ccs = []
for x in l:
    if x not in workers:
        if len(predecessors[x]) == 0:
            ccs.append(x)
while len(l) > 0:
    remove_ccs = []

    for i in range(len(workers)):
        if workers[i] == ".":
            if len(ccs) > 0:
                workers[i] = ccs[0]
                del (ccs[0])
        else:
            times[workers[i]] -= 1
            if times[workers[i]] == 0:
                remove_ccs.append(workers[i])

                for key, value in predecessors.items():
                    for cc in remove_ccs:
                        if cc in value:
                            value.remove(cc)

                for cc in remove_ccs:
                    result += cc

                for cc in remove_ccs:
                    if cc not in used and cc in successors.keys():
                        for c in successors[cc]:
                            if c not in added:
                                l.append(c)
                                added.add(c)

                for cc in remove_ccs:
                    used.add(cc)
                    l.remove(cc)

                l.sort()
                ccs = []
                for x in l:
                    if x not in workers:
                        if len(predecessors[x]) == 0:
                            ccs.append(x)

                if len(ccs) > 0:
                    workers[i] = ccs[0]
                    del (ccs[0])
                else:
                    workers[i] = "."

    print("{}\t\t".format(seconds), end='')
    for worker in workers:
        print("{}\t\t".format(worker), end='')
    print("{}\t\t".format(result))

    seconds += 1

print(result)
