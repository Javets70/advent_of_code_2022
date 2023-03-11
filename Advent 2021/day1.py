# data = open("./day1_sample_input.txt").readlines()
data = open("./day1_input.txt").readlines()
data = list(map(int, data))

count = 0
for i in range(len(data) - 1):
    if i > -1:
        if data[i + 1] > data[i]:
            count += 1

print("PART 1", count)

data2 = open("./day1_input.txt").readlines()
data2 = list(map(int, data2))

count2 = 0

for i in range(0, len(data2)):
    if i - 3 > -1:
        sum1 = sum(data2[i - 3: i])
        sum2 = sum(data2[i - 2: i + 1])
        if sum2 > sum1:
            count2 += 1

print("PART 2", count2)
