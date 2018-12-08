import InputHelper as iH

iH = iH.InputHelper(0)
lines = iH.lines

d = {}

child = True
metadata = False
counting = False
n_meta = 0
sum = 0

numbers = []
for line in lines:
    numbers_ = line.split()
    numbers = [int(x) for x in numbers_]

flag = False
i_father = 0
i_mdata = -1
i_child = -1
n_child = -1
n_data = -1
d = {}

counter = 1
print(numbers)
while len(numbers) > 0:
    for i, number_ in enumerate(numbers):

        if i % 2 == 0:
            i_child = i
            n_child = number_
        if i % 2 == 1:
            i_mdata = i
            n_data = number_

        data = []
        if i % 2 == 1:
            if n_child == 0:
                data = numbers[i_mdata + 1:i_mdata + 1 + n_data]
                for x in data:
                    sum += x
                numbers[i_father] -= 1

                print("Node:[", numbers[i_child], ",", numbers[i_mdata], ",", data, "]", ", Father:", i_father)

                for x in data:
                    del (numbers[i_mdata + 1])

                del (numbers[i_mdata])
                del (numbers[i_child])
                print(numbers)
                break

        if i % 2 == 1:
            i_father = i_child

print(sum)  # 54308
