data = open("./day2_input.txt").readlines()
x, y = 0, 0
for line in data:
    command, value = line.split()
    value = int(value)
    if command == "forward":
        x += value
    elif command == "down":
        y += value
    elif command == "up":
        y -= value
print("DAY2 PART1", x * y)

aim, x, y = 0, 0, 0

for line in data:
    command, value = line.split()
    value = int(value)
    if command == "forward":
        x += value
        y += aim * value
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value
print("DAY2 PART2", x * y)
