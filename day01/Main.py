import InputHelper as iH

iH = iH.InputHelper(1)
lines = iH.lines

sums = []
rsum = 0

while True:
    for line in lines:
        rsum += int(line)

        if rsum in sums:
            print(rsum)
            exit()

        sums.append(rsum)
