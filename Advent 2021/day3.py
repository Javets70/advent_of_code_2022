data = open("./day3_input.txt").readlines()
data = [i[:-1] for i in data]
columns = []

for i in range(len(data[0])):
    column = ""
    for j in range(len(data)):
        column += data[j][i]
    columns.append(column)

columns = columns[:-1]  # remove newline characters
gamma = ""
epsilon = ""
mid = int(len(columns[0]) / 2)
for i in columns:
    if i.count("0") > mid:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

epsilon = int(epsilon, 2)
gamma = int(gamma, 2)
print("DAY3 PART1", gamma * epsilon)


def get_common_bit(lst: list, pos: int, most_common=True):
    if len(lst) == 1:
        return lst[0][pos]

    column = ""
    for i in lst:
        column += i[pos]

    count1 = column.count("1")
    count0 = column.count("0")
    if most_common:
        if count1 >= count0:
            return "1"
        elif count0 > count1:
            return "0"
    else:
        if count0 <= count1:
            return "0"
        elif count1 < count0:
            return "1"


oxygen_nums = []
scrubber_nums = []


for i in range(len(data[0])):
    temp_oxygen_nums = []
    temp_scrubber_nums = []
    if oxygen_nums == []:
        most_common_bit = get_common_bit(data, 0)
        least_common_bit = get_common_bit(data, 0, False)

        for j in data:
            if j[i] == most_common_bit:
                oxygen_nums.append(j)
            if j[i] == least_common_bit:
                scrubber_nums.append(j)
    else:
        most_common_bit = get_common_bit(oxygen_nums, i)
        least_common_bit = get_common_bit(scrubber_nums, i, False)

        for num1 in oxygen_nums:
            if num1[i] == most_common_bit:
                temp_oxygen_nums.append(num1)

        for num2 in scrubber_nums:
            if num2[i] == least_common_bit:
                temp_scrubber_nums.append(num2)

        oxygen_nums = temp_oxygen_nums
        scrubber_nums = temp_scrubber_nums

print(oxygen_nums, scrubber_nums)
oxygen_nums = int(oxygen_nums[0], 2)
scrubber_nums = int(scrubber_nums[0], 2)
print("DAY 3 PART2", oxygen_nums * scrubber_nums)
