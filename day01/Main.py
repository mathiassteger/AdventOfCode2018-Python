import InputHelper as iH

iH = iH.InputHelper(1)
lines = iH.lines()

sums = []
sum = 0
boolean = True
while boolean:
    for line in lines:
        line = line.strip()
        if line[0] == "+":
            sum+= int(line[1:])
        else:
            sum-= int(line[1:])

        if sum in sums:
            boolean = False
            break

        sums.append(sum)

print(sum)
