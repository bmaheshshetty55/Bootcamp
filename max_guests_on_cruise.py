def max_guests_on_cruise(T, E, L):
    current_guests = 0
    max_guests = 0
    for i in range(T):
        current_guests += E[i] - L[i]
        if current_guests > max_guests:
            max_guests = current_guests
    return max_guests
T = 5
E = [7, 0, 5, 1, 3]
L = [1, 2, 1, 3, 4]
result = max_guests_on_cruise(T, E, L)
print(result)