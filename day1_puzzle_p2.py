f = open('puzzle_input.txt', 'r')

lines = f.readlines()
items = list(range(100))
length = len(items)

starting_value = 50
count = 0

for instruction in lines:
    for char in instruction.strip().split():
        direction = char[0]
        value = int(char[1:])
        if direction == 'R':
            count += (starting_value + value) // length
            starting_value = (starting_value + value) % length
        elif direction == 'L':
            if value > starting_value:
                count += (value - starting_value - 1) // length + 1
            starting_value = (starting_value - value) % length
            pass
print(count)
f.close()