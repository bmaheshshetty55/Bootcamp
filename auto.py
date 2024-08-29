import math
distance=0
charge=0
distance=float(input(" enter the distance: "))

if distance<=1.5:
    charge=35
else:
    d=distance-1.5
    d_ceil=math.ceil(d)
    print(d_ceil)
    c_new=25*d_ceil
    charge=35+c_new
print(charge)