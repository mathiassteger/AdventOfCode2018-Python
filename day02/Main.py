import InputHelper as iH

iH = iH.InputHelper(2)
lines = iH.lines

sum_two = 0
sum_three = 0
for line in lines:
    x = set(line)
    fount_two = False
    found_three = False
    for i in x:
        if not fount_two:
            if line.count(i) == 2:
                sum_two += 1
                fount_two = True
        if not found_three:
            if line.count(i) == 3:
                sum_three += 1
                found_three = True

print(sum_two * sum_three)

for line in lines:
    for line2 in lines:
        wrongs = 0
        for x, y in zip(line, line2):
            if x != y:
                wrongs += 1
        if wrongs == 1:
            print(line)
            print(line2)
            exit()
