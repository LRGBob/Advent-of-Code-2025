f = open('puzzle_sample.txt', 'r')

lines = f.readlines()
items = list(range(100))
length = len(items)

starting_value = 50
count = 0

for instruction in lines:
    rotation = instruction.strip().split()
    for char in rotation:
        if len(char) == 2:
            if char[0] == 'R':
                value = int(str(char[1]))       
                starting_value = (starting_value + value) % length
                if starting_value == 0:
                    count += 1 
            elif char[0] == 'L':
                value = int(str(char[1]))
                starting_value = (starting_value - value) % length
                if starting_value == 0:
                    count += 1        
        if len(char) == 3:
            if char[0] == 'R':
                value = int(str(char[1])+str(char[2]))    
                starting_value = (starting_value + value) % length
                if starting_value == 0:
                    count += 1             
            elif char[0] == 'L':
                value = int(str(char[1])+str(char[2]))      
                starting_value = (starting_value - value) % length
                if starting_value == 0:
                    count += 1 
        if len(char) == 4:
            if char[0] == 'R':
                value = int(str(char[1])+str(char[2])+str(char[3]))    
                starting_value = (starting_value + value) % length
                if starting_value == 0:
                    count += 1             
            elif char[0] == 'L':
                value = int(str(char[1])+str(char[2])+str(char[3]))      
                starting_value = (starting_value - value) % length
                if starting_value == 0:
                    count += 1
print(count)
f.close()