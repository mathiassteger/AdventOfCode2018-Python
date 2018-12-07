import InputHelper as iH

iH = iH.InputHelper(6)
lines = iH.lines
numbers = iH.numbers


def md(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


xs = []
ys = []
for line in numbers:
    x_, y_ = line
    xs.append(x_)
    ys.append(y_)

print(xs)
print(ys)

grid = []
gridsize = 360
for i in range(gridsize):
    grid.append([[(0, 0), 1e7] for x in range(gridsize)])

for x, y in zip(xs, ys):
    grid[y][x] = [(x, y), -1]

for i, y_ in enumerate(grid):
    for j, x_ in enumerate(grid[i]):
        cands = []
        mind = 1e7
        if grid[i][j][1] != -1:
            for x, y in zip(xs, ys):
                d = md((j, i), (x, y))

                if d < mind:
                    cands.clear()
                    mind = d
                    cands.append((x, y))
                elif d == mind:
                    cands.append((x, y))

            if len(cands) == 1:
                grid[i][j] = [cands[0], mind]
            elif len(cands) > 1:
                grid[i][j] = [(-2, -2), -2]

if gridsize < 20:
    for i in range(len(grid)):
        print("")
        for k in grid[i]:
            if -2 in k or -1 in k:
                print(str(k) + '\t', end='')
            else:
                print(str(k) + '\t\t', end='')

print("")
infs = []
fins = []
for i, y_ in enumerate(grid):
    for j, x_ in enumerate(grid[i]):
        if j == 0 or i == 0 or j == len(grid[i]) - 1 or i == len(grid) - 1:
            if x_[0] not in infs and x_[1] != -2:
                infs.append(x_[0])

for i, y_ in enumerate(grid):
    for j, x_ in enumerate(grid[i]):
        if j == 0 or i == 0 or j == len(grid[i]) - 1 or i == len(grid) - 1:
            pass
        else:
            if x_[0] not in fins and x_[0] not in infs and x_[1] != -2:
                fins.append(x_[0])

fin = (-1, -1)
lastmax = 0
for x in fins:
    max = 0
    for i, y_ in enumerate(grid):
        for j, x_ in enumerate(grid[i]):
            if grid[i][j][0] == x:
                max += 1

    if max > lastmax:
        fin = x
        lastmax = max

print("Result1:", fin, lastmax)  # 5941

regions = 0
for i in range(-500, 501):
    for j in range(-500, 501):
        sum = 0
        for x, y in zip(xs, ys):
            sum += md((i, j), (x, y))
        if sum < 10000:
            regions += 1

print("Result2:", regions)

'''
(331, 86) 1583  X
(228, 122) 1681 X
(205, 134) 1721 X
(141, 141) 1923 X
(183, 157) 2718 X
(125, 176) 2790 X
(240, 243) 4205 X
(190, 288) 5941 X
Result: (190, 288) 5941
'''

# 2 stars for finishing, 2 stars for each member you were faster than, so: -16 for me, -? for hwiards