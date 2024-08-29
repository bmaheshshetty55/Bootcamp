distance = 0
charge = 0
distance = float(input("Enter the distance: "))

if distance <= 1.5:
    charge = 35
else:
    d = distance - 1.5
    
    # Implementing ceiling without math.ceil
    d_ceil = int(d) if d == int(d) else int(d) + 1
    
    print(d_ceil)
    c_new = 25 * d_ceil
    charge = 35 + c_new

print(charge)
