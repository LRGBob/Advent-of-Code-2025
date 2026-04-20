items = list(range(100))
length = len(items)

starting_value = 50
myList = ['L55','R5','R10','L9','L1','R199','R1']
count = 0

for step in myList:
    if len(step) == 2:
        if step[0] == 'R':
            value = int(str(step[1]))       
            starting_value = (starting_value + value) % length
            if starting_value == 0:
                count += 1 
        elif step[0] == 'L':
            value = int(str(step[1]))
            starting_value = (starting_value - value) % length
            if starting_value == 0:
                count += 1        
    if len(step) == 3:
        if step[0] == 'R':
            value = int(str(step[1])+str(step[2]))    
            starting_value = (starting_value + value) % length
            if starting_value == 0:
                count += 1             
        elif step[0] == 'L':
            value = int(str(step[1])+str(step[2]))      
            starting_value = (starting_value - value) % length
            if starting_value == 0:
                count += 1 
    if len(step) == 4:
        if step[0] == 'R':
            value = int(str(step[1])+str(step[2])+str(step[3]))    
            starting_value = (starting_value + value) % length
            if starting_value == 0:
                count += 1             
        elif step[0] == 'L':
            value = int(str(step[1])+str(step[2])+str(step[3]))      
            starting_value = (starting_value - value) % length
            if starting_value == 0:
                count += 1
print(starting_value)
print(count)
# # Forward movement
# for i in range(length):
#     print(items[i % length]) # Results: a, b, c, a, b, c...

# # Backward movement
# index = 0
# for _ in range(length):
#     index = (index - 1) % length
#     print(items[index]) # Results: c, b, a, c, 