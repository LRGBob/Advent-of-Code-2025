items = list(range(100))
length = len(items)

starting_value = 50
value = [55, 33]

for step in value:
    starting_value = (starting_value + step) % length
    print(starting_value)

# # Forward movement
# for i in range(length):
#     print(items[i % length]) # Results: a, b, c, a, b, c...

# # Backward movement
# index = 0
# for _ in range(length):
#     index = (index - 1) % length
#     print(items[index]) # Results: c, b, a, c, 