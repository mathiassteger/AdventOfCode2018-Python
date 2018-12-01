import InputHelper as iH

iH = iH.InputHelper(1)
lines = iH.lines(do_strip=True)

sums = []
sum = 0

while True:
    for line in lines:
        if line[0] == "+":
            sum += int(line[1:])
        else:
            sum -= int(line[1:])

        if sum in sums:
            print(sum)
            exit()

        sums.append(sum)
