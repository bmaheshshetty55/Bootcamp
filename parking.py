def max_cars(arr):
    max_sequence = 0
    current_sequence = 0
    for slot in arr:
        if slot == 'S':
            current_sequence += 1
        else:
            current_sequence = 0
        max_sequence = max(max_sequence, current_sequence)
    return max_sequence

arr = ['S', 'S', 'X', 'S', 'S', 'S', 'X', 'S', 'S']
print(max_cars(arr))