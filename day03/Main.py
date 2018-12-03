import InputHelper as iH

iH = iH.InputHelper(3)
lines = iH.lines(do_strip=True)

ids = []
x = []
y = []
w = []
h = []

for line in lines:
    nosp = line.split(" ")
    ids.append(int(nosp[0][1:]))
    minmax = nosp[2][:-1].split(",")
    x.append(int(minmax[0]))
    y.append(int(minmax[1]))
    wh = nosp[3].split("x")
    w.append(int(wh[0]))
    h.append(int(wh[1]))

sizes = [o * q for o, q in zip(w, h)]
print(ids)
print(x)
print(y)
print(w)
print(h)
print(sizes)
graph = []

for i in range(1500):
    graph.append([])
    for j in range(1500):
        graph[i].append([0])

for id_, x_, y_, w_, h_ in zip(ids, x, y, w, h):
    for i in range(w_):
        for j in range(h_):
            graph[x_ + i][y_ + j][0] += 1
            graph[x_ + i][y_ + j].append(id_)

csum = 0

d = {}

for i in range(1500):
    for j in range(1500):
        if graph[i][j][0] > 1:
            csum += 1
        if len(graph[i][j]) == 2:
            idu = graph[i][j][1]
            if idu not in d:
                d[idu] = 1
            else:
                d[idu] += 1

for key in d:
    if d[key] in sizes:
        indices = [i + 1 for i, x in enumerate(sizes) if x == d[key]]
        # print(key, index, d[key])
        if key in indices:
            print("key:", key)

print('sum' + csum)  # 117175
