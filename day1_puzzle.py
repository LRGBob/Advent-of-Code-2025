f = open('puzzle_sample.txt', 'r')
lines = f.readlines()
starting_value = 50
count = 0
for instruction in lines:
    rotation = instruction.strip().split()
    print(rotation)
    for char in rotation:
        if len(char) == 2:
            if char[0] == 'R':
                value = int(str(char[1]))
                starting_value += value
                if starting_value == 0:
                    count += 1
            elif char[0] == 'L':
                value = int(str(char[1]))
                starting_value -= value
                if starting_value == 0:
                    count += 1            
        elif len(char) == 3:
            if char[0] == 'R':
                value = int(str(char[1]) + str(char[2]))
                starting_value += value
                if starting_value == 0:
                    count += 1              
            elif char[0] == 'L':
                value = int(str(char[1]) + str(char[2]))
                starting_value -= value
                if starting_value == 0:
                    count += 1
        elif len(char) == 4:
            if char[0] == 'R':
                value = int(str(char[1]) + str(char[2]) + str(char [3]))
                starting_value += value
                if starting_value == 0:
                    count += 1
            elif char[0] == 'L':
                value = int(str(char[1]) + str(char[2]) + str(char [3]))
                starting_value -= value
                if starting_value == 0:
                    count += 1
print(count)
f.close()