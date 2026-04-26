from tracemalloc import start


items = list(range(100))
length = len(items)

starting_value = 50
myList = ['R250']
count = 0

for step in myList:
    direction = step[0]
    value = int(step[1:])
    if direction == 'R':
        count += (starting_value + value) // length
        starting_value = (starting_value + value) % length
    elif direction == 'L':
        if value > starting_value:
            count += (value - starting_value - 1) // length + 1
        starting_value = (starting_value - value) % length
        pass

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