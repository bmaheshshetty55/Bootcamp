def find_vehicles(V, W):
    FW = (W - 2 * V) // 2
    TW = V - FW
    return TW, FW
V = 200
W = 540
TW, FW = find_vehicles(V, W)
print(f'TW = {TW} FW = {FW}')